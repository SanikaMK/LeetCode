class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_key_map = {"type": 0, "color": 1, "name":2}
        rule_index = rule_key_map[ruleKey]
        match_count = sum(item[rule_index] == ruleValue for item in items)
        return match_count
        