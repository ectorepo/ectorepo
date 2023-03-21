(use-modules (guix packages)
             (gnu packages android)
             (gnu packages python))

(let ((git-repo-with-path
       (manifest-entry
         (name "git-repo")
         (item git-repo)
         (version "2.4.1") ;most recent version
         (search-paths (list (search-path-specification
                              (variable "PYTHONPATH")
                              (files '("share/git-repo")))
                             (search-path-specification
                              (variable "GUIX_PYTHONPATH")
                              (files '("share/git-repo"))))))))

 (concatenate-manifests (list
                         (manifest
                          (list git-repo-with-path))
                          (packages->manifest
                           (list python)))))
