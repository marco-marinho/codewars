let rec digital_root (n : int) : int = 
  let rec aux acc = function
  | 0 -> if acc >= 10 then digital_root acc else acc
  | n -> aux (acc + (n mod 10)) (n / 10)
  in
  aux 0 n
