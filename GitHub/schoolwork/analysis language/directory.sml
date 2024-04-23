datatype entry = File of string | Folder of string * entry list;

val files = Folder("d1",
	[File "f1",
	Folder("d2",
		[File "f2",
		Folder("d3",
			[File "f3"])]),
	File "f4",
	Folder("d3",
		[File "f5"])]);

fun get_entries (File fname) = [fname]
|   get_entries (Folder(dname, cnts)) = dname::(get_contents cnts)
and
	get_contents L = foldr (fn (e,sofar) => get_entries e @ sofar) [] L;

get_entries files;

(* Output:
val it = ["d1","f1","d2","f2","d3","f3","f4","d3","f5"] : string list
*)

(* Directory Structure for above:

d1
	f1
	d2
		f2
		d3
			f3
	f4
	d3
		f5

*)