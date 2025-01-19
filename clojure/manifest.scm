(use-modules (guix packages)
             (guix transformations)
             (gnu packages clojure)
             ;; (ellipsis packages clojure)
             )

;; ;; the main difference for clojure-ellipsis is that it's built using
;; ;; [tools.namespace "1.4.5"] and [tools.reader "1.3.7"]
;; (define upgrade-clojure-deps
;;   ;; p-i-r/spec doesn't operate by identity
;;   ;; (package-input-rewriting/spec `(("clojure" . ,(const clojure-ellipsis))))
;;   (package-input-rewriting `((,clojure . ,clojure-ellipsis))))

(packages->manifest
 (map identity ;; upgrade-clojure-deps
      ;; deps for clojure-tools
      (list
            clojure-tools-deps-alpha
            ;; clojure-tools
            clojure-tools-cli
            clojure-data-xml
            clojure-data-codec
            clojure-test-check
            clojure-tools-gitlibs

            ;; algo-monads
            clojure-algo-monads
            clojure-tools-macro

            ;; no deps
            clojure-algo-generic
            clojure-core-match
            clojure-instaparse
            clojure-data-csv)))

;; "GNU Emacs 29.1 (build 1, x86_64-pc-linux-gnu, GTK+ Version 3.24.37, cairo version 1.16.0)"

