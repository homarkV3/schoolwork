(* stream.sml: Based on work on streams in Abelson and Sussman *)
datatype 'a stream  = Nil | Cons of 'a * (unit -> 'a stream); 

fun force f = f ();		(* Call a function with a unit (no args) *)

fun head Nil = raise Empty
|   head (Cons(h,_)) = h; 

fun tail Nil = Nil
|   tail (Cons(_,t)) = force t;

fun next Nil = raise Empty
|   next c = head (tail c);

(* take stops after the nth Cons *)
fun take _ Nil = Nil
|   take 0 _ = Nil
|   take n (Cons(h,t)) = Cons (h, fn () => take (n-1) (force t));

(* drop gives the nth Cons *)
fun drop _ Nil = Nil
|   drop 0 strm = strm
|   drop n (Cons(_,t)) = drop (n-1) (force t);

(* nth gives the nth value *)
fun nth 0 s = head s
|   nth n s = nth (n-1) (tail s);

fun filter_ _ Nil = Nil
|   filter_ f (Cons (h,t)) =
	if (f h) then
		Cons (h, fn () => filter_ f (force t))
    else
		filter_ f (force t);

fun map_ _ Nil = Nil
|   map_ f (Cons(h,t)) = Cons(f h, fn () => map_ f (force t));

(* foldl_ gives a stream of intermediate results *)
fun foldl_ _ c Nil = Cons(c, fn () => Nil)
|   foldl_ f c (Cons(h,t)) =
	let
		val v = f (h,c)
	in
		Cons(v, fn () => foldl_ f v (force t))
	end;

fun strm2list _ Nil = nil
|   strm2list 0 _ = nil
|   strm2list n (Cons(h,t)) = h::(strm2list (n-1) (force t));

fun list2strm nil = Nil
|   list2strm (h::t) = Cons(h, fn () => list2strm t);

fun app_n _ _ Nil = ()
|   app_n 0 _ strm = ()
|   app_n n f (Cons(x,t)) = (f x; app_n (n-1) f (force t));

fun print_int n = print (Int.toString n ^ "\n");
fun printStrm n strm = app_n n print_int strm;
