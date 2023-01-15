class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else str(x)[::-1] == str(x) 

def main():
    """Проверка алгоритма"""
    input = 121
    S = Solution()
    print(S.isPalindrome(input))

if __name__ == "__main__":
    main()