class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = list(range(1, m + 1))
        answer = []

        for q in queries:
            idx = P.index(q)      # 현재 위치 찾기
            answer.append(idx)    # 위치 저장

            P.pop(idx)            # 기존 위치에서 제거
            P.insert(0, q)        # 맨 앞으로 이동

        return answer