let map_add m x =
  let rec aux acc = function
    | [] -> (x, 1) :: acc
    | (c, n) as h :: t ->
      if c = x then
        (c, n + 1) :: (t @ acc) 
      else
        aux (h::acc) t
      in
    aux [] m
    

let string_to_count s =
  let rec aux acc i =
    if i >= String.length s then acc
    else
      let c = s.[i] in
      if c >= 'a' && c <= 'z' then
        let acc = map_add acc c in
        aux acc (i + 1)
      else
        aux acc (i + 1)
      in
    aux [] 0

let rec repeat (c, n) =
  if n = 0 then ""
  else (String.make 1 c) ^ repeat (c, (n - 1))

let sorter (c1, n1) (c2, n2) = if n1 > n2 then -1 else if n1 < n2 then 1 else if c1 < c2 then -1 else 1
let other_sorter s1 s2 = if String.length s1 > String.length s2 then -1 else if String.length s1 < String.length s2 then 1 else String.compare s1 s2

let filter (_, n) = n > 1

let remove_less l1 l2 =
  let rec keep (c, n) = function
  | [] -> true
  | (a, b) :: _ when c = a -> n > b || n = b
  | h :: t -> keep (c, n) t
in
 List.filter (fun x -> keep x l2) l1

let mix (ss1: string) (ss2: string) =
  let a = List.filter filter (List.sort sorter (string_to_count ss1))
in
  let b = List.filter filter (List.sort sorter (string_to_count ss2))
in
  let s1 = remove_less a b in
  let s2 = remove_less b a in
  let rec aux acc x y = 
    match x, y with
    | (c1, n1) :: t1, (((c2, n2) :: _) as l2) when n1 > n2 || (n1 = n2 && c1 < c2) -> aux (("1:" ^ repeat (c1, n1)) :: acc) t1 l2
    | ((c1, n1) :: _) as l1, (c2, n2) :: t2 when n1 < n2 || (n1 = n2 && c2 < c1) -> aux (("2:" ^ repeat (c2, n2)) :: acc) l1 t2
    | (c1, n1) :: t1, (c2, n2) :: t2 when c1 = c2 && n1 = n2 -> aux (("=:" ^ repeat (c1, n1)) :: acc) t1 t2
    | (c1, n1) :: t1, [] -> aux (("1:" ^ repeat (c1, n1)) :: acc) t1 []
    | [], (c2, n2) :: t2 -> aux (("2:" ^ repeat (c2, n2)) :: acc) [] t2
    | [] , [] -> acc
    | _ , _ -> acc
    in
  let parts = List.sort other_sorter (aux [] s1 s2)
  in
  List.fold_left (fun acc x -> if acc = "" then x else acc ^ "/" ^ x) "" parts
