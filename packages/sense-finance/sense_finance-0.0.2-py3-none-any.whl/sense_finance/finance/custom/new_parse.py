from pyparsing import *
from sense_finance.finance.custom.common import *
from sense_finance.finance.custom.core import *
from sense_finance.finance.target.base_parser import BaseExpressParser


class TargetExpressParser(BaseExpressParser):

    def __init__(self, text, model_class):
        super(TargetExpressParser, self).__init__(text, model_class)

    def _find_high_level_operator_index(self, text, start):
        for i in range(start, len(text)):
            if text[i] == '*' or text[i] == '/':
                return i
        return -1

    def _find_next_operator_index(self, text, start):
        left_bracket_count = 0
        high_operator_num = 0
        for i in range(start, len(text)):
            c = text[i]
            if c == '(':
                left_bracket_count += 1
                continue
            if c == ')':
                left_bracket_count -= 1
                if left_bracket_count < 0:
                    if high_operator_num > 0:
                        return i
                    return -1
            if left_bracket_count > 0:
                continue
            if c == '+' or c == '-':
                return i
            if c == '*' or c == '/':
                high_operator_num += 1
        return len(text)

    def _find_low_level_operator_index(self, text, index):
        if index <= 1:
            return -1
        right_bracket_count = 0
        for i in range(index - 1, 0, -1):
            c = text[i]
            if c == ')':
                right_bracket_count += 1
                continue
            if c == '(':
                right_bracket_count -= 1
                if right_bracket_count < 0:
                    return -1
            if right_bracket_count > 0:
                continue
            if c == '*' or c == '/':
                return -1
            if c == '+' or c == '-':
                return i
        return -1

    def rebuild_express_text(self, text):
        index = 0
        while True:
            index = self._find_high_level_operator_index(text, index)
            if index < 0:
                return text
            low_index = self._find_low_level_operator_index(text, index)
            if low_index < 0:
                index += 1
                continue
            next_index = self._find_next_operator_index(text, index)
            if next_index < 0:
                return text
            text1 = text[0:low_index + 1] + '(' + text[low_index + 1:next_index] + ')'
            if next_index < len(text):
                text1 += text[next_index:len(text)]
            text = text1
            if next_index >= len(text) - 1:
                return text
            index = next_index

    def parse_express(self):
        try:
            text = self.rebuild_express_text(self.text)
            if sd.is_debug():
                sd.log_info("rebuild_express_text got text={}".format(text))
            if text != self.text:
                sd.log_info("rebuild_express_text for {0} got {1}".format(self.text, text))
            exp = Forward()
            LPAR, RPAR = map(Suppress, "()")
            word = Regex(r'(?!abs)(?!sqrt)(?!zero)(?![\+\-\*/\(\)])[\u4e00-\u9fa5、:\w\.]+')
            keyword = Regex(r'abs|zero|sqrt')
            group = Optional(keyword) + Group(LPAR + exp + RPAR)
            term = word | group | keyword
            operator = Word("+-*/", max=1)
            exp << term + ZeroOrMore(operator + term)
            items = exp.parseString(text, parseAll=True).asList()
            sd.log_info("parse {0} got {1}".format(text, items))
            return items
        except Exception as ex:
            sd.log_exception(ex)
            sd.log_info("parse target express failed {}".format(text))
            self.error = "指标公式解析失败"
            return None

    def convert_result(self, items, result):
        operator = None
        convert_word = None
        lost_word = None
        for item in items:
            if not self.is_valid_token(item, operator, convert_word, result):
                return None
            if self.is_nest_item(item):
                express = self._add_express(result, item, operator, convert_word)
                if not express:
                    return None
                operator, convert_word = None, None
                continue
            if is_target_operator(item):
                operator = item
                continue
            if is_target_convert_word(item):
                convert_word = item
                continue
            target_item = build_target_item(item, operator, convert_word, lost_word)
            if not target_item:
                sd.log_info("build target_item failed for {}".format(item))
                return None
            target_item.depth = result.depth + 1
            result.add(target_item)
            operator, convert_word = None, None
        return result

    def _is_valid_operator(self, result, item, operator):
        if len(result) > 0 and operator is None:
            sd.log_info(
                "_add_express not well with len={0} and operator={1} item={2}".format(len(result), operator, item))
            return False
        if len(result) == 0 and operator is not None:
            sd.log_info(
                "_add_express not well with len={0} and operator={1} item={2}".format(len(result), operator, item))
            return False
        return True

    def _add_express(self, result, item, operator, convert_word, lost_word=None):
        convert_type = convert_target_convert_type(convert_word)
        lost_type = convert_target_lost_type(lost_word)
        express = self.convert_result(item, CompositeExpress(operator, lost_type, convert_type, result.depth + 1))
        if not express:
            return None
        result.add(express)
        return express

    def is_valid_token(self, item, operator, convert_word, result):
        if is_target_operator(item):
            if operator:
                sd.log_info("dup operator {}".format(self.text))
                return False
            return True
        if is_target_convert_word(item):
            if convert_word:
                sd.log_info("dup convert_word {}".format(self.text))
                return False
            return True
        if len(result) > 0 and operator is None:
            sd.log_info(
                "_add_express not well with len={0} and operator={1} item={2}".format(len(result), operator, item))
            return False
        if len(result) == 0 and operator is not None:
            sd.log_info(
                "_add_express not well with len={0} and operator={1} item={2}".format(len(result), operator, item))
            return False
        return True
