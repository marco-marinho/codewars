#include <vector>

std::vector<int> move_zeroes(const std::vector<int>& input) {
  std::vector<int> output(input.size(), 0);
  int insertion_idx = 0;
  for (size_t i = 0; i < input.size(); i++){
    if (input[i] != 0){
      output[insertion_idx++] = input[i];
    }
  }
  return output;
}