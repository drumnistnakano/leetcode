/*
 * @lc app=leetcode id=347 lang=typescript
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
function topKFrequent(nums: number[], k: number): number[] {
  // 各数値をグループ化する配列
  const array: [
    {
      no: number;
      count: number;
    }
  ] = [{ no: nums[0], count: 0 }];

  nums.map((num, index) => {
    let exsistNum = false;
    array.map((obj) => {
      if (num === obj.no) {
        obj.count += 1;
        exsistNum = true;
      }
    });

    if (!exsistNum) {
      array.push({ no: num, count: 1 });
    }
  });

  // 配列内のcount数のオブジェクトをソートして、k個分のオブジェクトのみ取り出す
  array.sort((a, b) => {
    return b.count - a.count;
  });
  const topKFrequentArray = array.slice(0, k);

  return [...topKFrequentArray.map((kobj) => kobj.no)];
}

// @lc code=end
