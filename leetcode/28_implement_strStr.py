# -*- coding: utf-8 -*-
"""
28.实现strStr()函数
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        思路:滑动窗口,以needle的长度作为窗口大小,遍历haystack进行逐个对比.滑动窗口L,字符串长度N
        时间复杂度:O((N-L)*L),内循环中比较子串复杂度为L,总共需要比较(N-L)次.
        空间复杂度:常量空间
        缺陷:会将haystack中所有长度为L的子串都与needle相比较.实际上只需要子串的第一个字符与needle字符串第一个字符串相同时才需要比较.
        """
        if not needle:
            return 0
        length = len(needle)
        n = len(haystack)
        for i in range(n - length + 1):
            if haystack[i:i+length] == needle:
                return i
        return -1

    def strStr2(self, haystack, needle):
        """
        思路:滑动窗口改进,只有当遍历haystack字符与needle第一个字符相同时,才进行对比.否则继续遍历,直到结束
        时间复杂度:O((N-L)*L)外层遍历最坏遍历(N-L)次,内层比较L次.即(N-L)*L
        空间复杂度:常量空间复杂度
        """
        if not needle:
            return 0
        n = len(haystack)
        l = len(needle)
        for i in range(n - l + 1):
            if haystack[i] == needle[0]:
                if haystack[i:i+l] == needle:
                    return i
        return -1

    def strStr3(self, haystack, needle):
        """
        思路:双指针法.haystack指针pn找到与needle第一个字符一样的,然后两个指针迭代记录迭代长度,迭代完成后比较cur_len是否与needle长度相当,
        相同则返回pn-l位置索引;不相同,则pn进行回溯,回溯应该pn-cur_len+1.
        时间复杂度:最坏O((N-L)*L),最优O(N)
        空间复杂度:O(1)
        """
        l, n = len(needle), len(haystack)
        if l == 0:
            return 0
        # haystack指针
        pn = 0
        while pn < n - l + 1:
            # 首先,找到haystack中字符与needle首字符一致的
            while pn < n - l + 1 and haystack[pn] != needle[0]:
                pn += 1
            # 然后,needle指针置为0,开始双指针迭代
            curr_len = pl = 0
            while pl < l and pn < n and haystack[pn] == needle[pl]:
                pl += 1
                pn += 1
                curr_len += 1
            # 当相同字符长度与needle长度一致时,即找到索引位置
            if curr_len == l:
                return pn - l
            # 不一致,则进行回溯
            pn = pn - curr_len + 1
        return -1

    def strStr4(self, haystack, needle):
        """
        思路:使用子串的哈希值与needle串哈希值相比较,哈希值计算复杂度需要通过滚动哈希值计算方式进行优化为常量级.
        通过取模避免数值溢出.
        时间复杂度:O(N) 计算needle哈希值需要O(L),执行N-L次循环,每次循环计算复杂度为常数
        空间复杂度:O(1)
        """
        L, n = len(needle), len(haystack)
        if L > n:
            return -1

        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2 ** 31

        # lambda-function to convert character to integer
        h_to_int = lambda i: ord(haystack[i]) - ord('hardware')
        needle_to_int = lambda i: ord(needle[i]) - ord('hardware')

        # compute the hash of strings haystack[:L], needle[:L]
        h = ref_h = 0
        for i in range(L):
            h = (h * a + h_to_int(i)) % modulus
            ref_h = (ref_h * a + needle_to_int(i)) % modulus
        if h == ref_h:
            return 0

        # const value to be used often : hardware**L % modulus
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
            if h == ref_h:
                return start

        return -1

    def strStr5(self, haystack, needle):
        pass


if __name__ == '__main__':
    haystack = "hello"
    needle = "hardware"
    print(Solution().strStr4(haystack, needle))
