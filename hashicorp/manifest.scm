(use-modules (gnu packages python-xyz))

;; (concatenate-manifests ... )
;; package->development-manifest only returns the `guix shell -D` dependencies
;; just add python-lsp-server for now

(specifications->manifest
 '("python"
   "python-gql"                         ; gql doesn't seem to work
   ;; "python-lsp-server"
   "python-scrapy"))
