#Solution



class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque([start])
        visited = set()
        visited.add(start)
        while q:
            i = q.popleft()

            if arr[i] == 0:
                return True

            left = i + arr[i]
            right = i - arr[i]

            if 0<= left < n and left not in visited:
                visited.add(left)
                q.append(left)

            if 0<= right < n and right not in visited:
                visited.add(right)
                q.append(right)

        return False