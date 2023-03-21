(use-modules (guix packages)
             (gnu packages android)
             (gnu packages python))

(let ((git-repo-with-path
       (manifest-entry
         (name "git-repo")
         (item git-repo)
         (version "42")
         (search-paths (list (search-path-specification
                              (variable "PYTHONPATH")
                              (files '("share/git-repo")))
                             (search-path-specification
                              (variable "GUIX_PYTHONPATH")
                              (files '("share/git-repo"))))))))

 (concatenate-manifests (list
                         (manifest
;                          (list git-repo-with-path python))
                          (list git-repo-with-path))
                          (packages->manifest (list python
                                                    ;git-repo-with-path
                                                    ))

                         ))

  )
