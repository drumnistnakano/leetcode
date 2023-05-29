/*
 * @lc app=leetcode id=49 lang=typescript
 *
 * [49] Group Anagrams
 */

// @lc code=start
function groupAnagrams(strs: string[]): string[][] {
  const hash: {
    [key: string]: string[];
  } = {};

  strs.map((value, index) => {
    let exsistAnagram = false;
    Object.keys(hash).map((key) => {
      if (isAnagram(value, key)) {
        hash[key].push(value);
        exsistAnagram = true;
      }
    });

    if (!exsistAnagram) {
      hash[value] = [value];
    }
  });

  return [...Object.keys(hash).map((k) => hash[k])];
}

function isAnagram(value: string, key: string): boolean {
  if (value.length !== key.length) return false;

  var first: Array<string | null> = value.split("");
  const second = key.split("");

  for (let i = 0; i < second.length; i++) {
    const element = second[i];

    let found = first.indexOf(element);

    if (found !== -1) {
      first[found] = null;
    } else {
      return false;
    }
  }
  return true;
}

// @lc code=end
