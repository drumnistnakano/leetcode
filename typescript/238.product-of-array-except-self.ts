/*
 * @lc app=leetcode id=238 lang=typescript
 *
 * [238] Product of Array Except Self
 */

// @lc code=start
function productExceptSelf(nums: number[]): number[] {
  const hash: {
    [key: string]: number[];
  } = {};
  nums.map((value, index) => {
    hash[index.toString()] = nums.filter((element, j) => j !== index);
  });

  let array: number[] = [];
  Object.keys(hash).map((key) => {
    array.push(
      hash[key].reduce((product, currentValue) => product * currentValue)
    );
  });

  return array;
}
// @lc code=end
