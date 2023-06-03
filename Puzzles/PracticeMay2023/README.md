# Practice Exercises!

## 1. Merge Strings Alternately

### Status: ✅

You are given two strings, `word1` and `word2`. Merge the strings by adding letters
in alternating order, starting with `word1`. If a string is longer than the other,
append the additional letters onto the end of the merged string.

_Return the merged string._

### Example 1:
```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
```
Explanation: The merged string will be merged as so:
```
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```

### Example 2:
```
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
```
Explanation: Notice that as `word2` is longer, "rs" is appended to the end.
```
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
```

### Example 3:

```
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
```
Explanation: Notice that as `word1` is longer, "cd" is appended to the end.
```
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
```

### Constraints:

* `1 <= word1.length`, `word2.length <= 100`
* `word1` and `word2` consist of lowercase English letters.

### Acceptance Rate:
`82.8%`


* * *


## 2. Greatest Common Divisor of Strings

### Status: ✅

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + ... + t` (_i.e._, `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, _return the largest string `x` such that `x` divides both `str1` and `str2`_.

### Example 1:
```
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```

### Example 2:
```
Input: str1 = "ABABAB"`, `str2 = "ABAB"
Output: "AB"
```

### Example 3:
```
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

### Constraints:

* `1 <= str1.length`, `str2.length <= 1000`
* `str1` and `str2` consist of English uppercase letters.

### Acceptance Rate
`56.5%`


* * *


## 3. Kids With the Greatest Number of Candies

### Status: ✅

There are `n` kids with candies. You are given an integer array of candies, where each `candies[i]` represents the number of candies the `i`th kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

_Return a boolean array result of length `n`, where `result[i]` is true if, after giving the ith kid all the `extraCandies`, they will have the greatest number of candies among all the kids, or false otherwise._

> Note that multiple kids can have the greatest number of candies.

### Example 1:
```
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
```
Explanation: If you give all `extraCandies` to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

### Example 2:
```
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
```
Explanation: There is only 1 extra candy.

Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

### Example 3:
```
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```

### Constraints:
* `n == candies.length`
* `2 <= n <= 100`
* `1 <= candies[i] <= 100`
* `1 <= extraCandies <= 50`

### Acceptance Rate
`88.0%`


* * *


## 4. Can Place Flowers

### Status: ✅

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return true if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise. 

### Example 1:
```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
```

### Example 2:
```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
```

### Constraints:

* `1 <= flowerbed.length <= 2 * 104`
* `flowerbed[i]` is `0` or `1`.
* There are no two adjacent flowers in `flowerbed`.
* `0 <= n <= flowerbed.length`

### Acceptance Rate
`32.7%`

* * *


## 5. Reverse Vowels of a String

### Status: ✅

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

### Example 1:
```
Input: s = "hello"
Output: "holle"
```

### Example 2:
```
Input: s = "leetcode"
Output: "leotcede"
```

### Constraints:

* `1 <= s.length <= 3 * 105`
* `s` consist of printable ASCII characters

### Acceptance Rate
`50.3%`


* * *


## 6. Reverse Words in a String

### Status: ✅

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

### Example 1:
```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

### Example 2:
```
Input: s = "  hello world  "
Output: "world hello"
```
**Explanation:** Your reversed string should not contain leading or trailing spaces.

### Example 3:
```
Input: s = "a good   example"
Output: "example good a"
```
**Explanation:** You need to reduce multiple spaces between two words to a single space in the reversed string.

### Constraints:

* `1 <= s.length <= 104`
* `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
* There is at least one word in `s`.

**Follow-up:** If the string data type is mutable in your language, can you solve it in-place with `O(1)` extra space?

### Acceptance Rate
`33.3%`


* * *


## 7. Product of Array Except Self

### Status: ❌

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

### Example 1:
```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

### Example 2:
```
Input: s = "  hello world  "
Output: "world hello"
```
**Explanation:** Your reversed string should not contain leading or trailing spaces.

### Example 3:
```
Input: s = "a good   example"
Output: "example good a"
```
**Explanation:** You need to reduce multiple spaces between two words to a single space in the reversed string.

### Constraints:

* `1 <= s.length <= 104`
* `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
* There is at least one word in `s`.

**Follow-up:** If the string data type is mutable in your language, can you solve it in-place with `O(1)` extra space?

### Acceptance Rate
`33.3%`


* * *


## 8. Move Zeroes

### Status: ✅

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

### Example 1:
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

### Example 2:
```
Input: nums = [0]
Output: [0]
```

### Constraints:

* `1 <= nums.length <= 104`
* `-231 <= nums[i] <= 231 - 1`

**Follow-up:** Could you minimize the total number of operations done?

### Acceptance Rate
`61.4%`
