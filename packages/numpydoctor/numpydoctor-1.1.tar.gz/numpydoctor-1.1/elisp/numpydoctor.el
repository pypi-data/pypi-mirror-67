;;; numpydoctor.el --- Emacs wrapper for numpydoctor
;;; Commentary:
;;; Automatic completion, correction, and checking of numpydoc-style
;;; python docstrings in Emacs.  This package is a thin wrapper around
;;; the `numpydoctor` python package and its command-line tool.
;;;
;;; Usage:
;;; Copy this file to your Emacs load path and add bindings in your
;;; python- or elpy-mode hook as you see fit. For example:
;;;
;;;    (defun my-elpy-mode-hook ()
;;;        (interactive)
;;;        (require 'numpydoctor)
;;;        (define-key elpy-mode-map (kbd "M-e") 'numpydoctor-check-at-point)
;;;        (define-key elpy-mode-map (kbd "M-d") 'numpydoctor-fix-at-point)
;;;        (define-key elpy-mode-map (kbd "M-E") 'numpydoctor-check-buffer)
;;;        (define-key elpy-mode-map (kbd "M-D") 'numpydoctor-fix-buffer))
;;;    (add-hook 'elpy-mode-hook 'my-elpy-mode-hook)

;;; Code:

(defgroup numpydoctor nil
    "Automatically build numpydoc-style python docstrings."
    :link '(emacs-library-link :tag "Source Lisp File" "numpydoctor.el")
    :version "26.3"
    :group 'python)

(defcustom numpydoctor-todo-level-default 2
    "TODO level when not explicitly specified.
This controls where TODO markers will be emitted when generated
docstrings are missing information. This value corresponds to the
-T/--todo argument to `numpydoctor`.

At TODO level 0, put TODO markers only on required missing
information, such as summaries, parameter names, and return types.
At level 1, put TODOs on missing parameter types.
At level 2, put TODOs on missing descriptions.
At level 3, put TODOs on missing return names.
At level 4, put TODOs on extended summary sections.

Each level implicitly includes the behaviors of all prior levels."
    :group 'numpydoctor)

(defcustom numpydoctor-line-wrap-col nil
    "Column at which emitted docstring lines will be wrapped.
If nil, defaults to the value of `fill-column`"
    :group 'numpydoctor)

(defcustom numpydoctor-indent-size nil
    "Column at which emitted docstring lines will be wrapped.
If nil, default to the value of `python-indent-offset`"
    :group 'numpydoctor)

(defun numpydoctor--sanity-check ()
    (if (eq (shell-command "which numpydoctor > /dev/null") 0)
        t
        (message "Could not find `numpydoctor` in path (hint: `pip install numpydoctor`)")))

(defun numpydoctor--join-non-nil (s)
    (string-join (seq-filter 'identity s) " "))

(defun numpydoctor--build-command (cmd &optional private magic nested offset)
    (numpydoctor--join-non-nil
        (list "numpydoctor"
            (if private "--private" nil)
            (if magic "--magic" nil)
            (if nested "--nested" nil)
            cmd
            (if offset (format "--offset=%d" offset) nil))))

(defun numpydoctor--build-check (&optional private magic nested offset missing)
    (numpydoctor--join-non-nil
        (list (numpydoctor--build-command "check" private magic nested offset)
            (if missing "--missing" nil))))

(defun numpydoctor--build-fix (&optional private magic nested offset missing todo-level)
    (numpydoctor--join-non-nil
        (list (numpydoctor--build-command "fix" private magic nested offset)
            (if missing "--missing" nil)
            (format "--line-wrap-col=%d" (or numpydoctor-line-wrap-col fill-column))
            (format "--indent-size=%d" (or numpydoctor-indent-size python-indent-offset))
            (let ((todo-level (or todo-level numpydoctor-todo-level-default)))
                (if (> todo-level 0)
                    (format "-%s" (make-string todo-level ?T)))))))

(defun numpydoctor--run-command-on-buffer (cmd &optional replace)
    (if (numpydoctor--sanity-check)
        (shell-command-on-region (point-min) (point-max)
            cmd
            nil
            replace
            "*numpydoctor error buffer*"))
    (if replace (deactivate-mark)))

(defun numpydoctor-check-buffer (&optional private magic nested)
    "Check all python docstrings in the current buffer.
Which docstrings are checked can be controlled with the arguments
PRIVATE, MAGIC, and NESTED, which allow checking private names, magic
names, and definitions nested in functions, respectively."
    (interactive)
    (numpydoctor--run-command-on-buffer
        (numpydoctor--build-check private magic nested)
        nil))

(defun numpydoctor-check-at-point (p)
    "Check the python docstring of the definition enclosing P."
    (interactive "d")
    (numpydoctor--run-command-on-buffer
        (numpydoctor--build-check t t t p)
        nil))

(defun numpydoctor-fix-buffer (&optional private magic nested todo-level)
    "Fix all python docstrings in the current buffer.
Which docstrings are checked can be controlled with the arguments
PRIVATE, MAGIC, and NESTED, which allow checking private names, magic
names, and definitions nested in functions, respectively."
    (interactive)
    (numpydoctor--run-command-on-buffer
        (numpydoctor--build-fix private magic nested nil nil todo-level)
        t))

(defun numpydoctor-fix-at-point (p &optional todo-level)
    "Fix the python docstring of the definition enclosing P."
    (interactive "d")
    (numpydoctor--run-command-on-buffer
        (numpydoctor--build-fix t t t p nil todo-level)
        t)
    (goto-char p))

(provide 'numpydoctor)
;;; numpydoctor.el ends here
