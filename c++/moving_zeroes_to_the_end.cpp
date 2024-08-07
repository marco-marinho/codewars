#include <vector>

std::vector<int> move_zeroes(const std::vector<int>& input) {
  std::vector<int> output(input.size(), 0);
  int insertion_idx = 0;
  for (int i : input){
    if (i != 0){
      output[insertion_idx++] = i;
    }
  }
  return output;
}