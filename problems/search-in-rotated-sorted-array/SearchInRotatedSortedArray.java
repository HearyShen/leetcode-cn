public class SearchInRotatedSortedArray {
    public static void main(String[] args) {
        int[][] nums = {{4, 5, 6, 7, 0, 1, 2}, {4, 5, 6, 7, 0, 1, 2}, {}, {1, 3}, {1, 3}};
        int[] targets = {0, 3, 5, 1, 0};
        int[] ans = {4, -1, -1, 0, -1};
        int ret;

        for (int i = 0; i < ans.length; i++) {
            ret = new Solution().search(nums[i], targets[i]);
            System.out.printf("{%d: %s}: return {%d}.\n", i, ret == ans[i], ret);
        }
    }
}

class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 0){
            return -1;
        }
        return binarySearch(nums, 0, nums.length - 1, target);
    }

    public int binarySearch(int[] nums, int left, int right, int target) {
        // boundary conditions
        if (left == right) {
            if (nums[left] == target) {
                return left;
            } else {
                return -1;
            }
        }
        else if (left + 1 == right){
            if (nums[left] == target){
                return left;
            }
            else if (nums[right] == target){
                return right;
            }
            else {
                return -1;
            }
        }

        // normal conditions
        int mid = left + (right - left) / 2;
        if (nums[0] <= nums[mid] && nums[mid] <= nums[right]) {
            if (target < nums[mid]) {
                return binarySearch(nums, left, mid - 1, target);
            } else if (nums[mid] < target) {
                return binarySearch(nums, mid + 1, right, target);
            } else {
                return mid;
            }
        } else if (nums[0] < nums[mid] && nums[mid] > nums[right]) {
            if (target == nums[mid]){
                return mid;
            } else if (nums[0] <= target && target < nums[mid]) {
                return binarySearch(nums, left, mid - 1, target);
            } else {
                return binarySearch(nums, mid + 1, right, target);
            }

        } else if (nums[0] > nums[mid] && nums[mid] < nums[right]) {
            if (target == nums[mid]){
                return mid;
            } else if (nums[mid] < target && target <= nums[right]) {
                return binarySearch(nums, mid + 1, right, target);
            } else {
                return binarySearch(nums, left, mid - 1, target);
            }
        }
        return -1;
    }
}