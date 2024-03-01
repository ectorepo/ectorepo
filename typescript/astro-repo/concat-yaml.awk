BEGIN { count=0 }
($0 ~/^---/) { ++count; }
(count % 2 == 1) { print $0; }
(count % 2 == 0) { next; }
