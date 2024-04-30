#! /bin/awk -f
# Here I only ensure the big differences in `id2c "./compare_bmk.awk -v summary=1 mcs.bmk" "./compare_bmk.awk -v summary=1 mcs_2018.bmk" | less_n`
# are checked, i.e. chapter 7, 8.
######################
# See py version for input file generation
# problems:
# 1. some texts are dropped like the block 'For example, in the base case of the deﬁnition of concatenation 7.1.3 ...'
######################
# Run `. ~/.virtualenv/misc/bin/activate; icdiff mcs-unlocked.txt mcs_2018-unlocked.txt | awk -f diff_pdf_text.awk | less_n`.
function reset_total_mod()
{
  # print "reset_total_mod"
  total_mod=""
  find_total_add_file_idx=0
}
BEGIN {
  # This is got from google AI
  ansi_prefix="\x1b\\["
  orange_color="0;34m"
  all_foreground_color=ansi_prefix"[0-9]+;[0-9]+m"
  all_background_color=ansi_prefix"7;[0-9]+;[0-9]+m"
  all_color="(" all_foreground_color "|" all_background_color ")"
  reset_color=ansi_prefix"m"
  # block_delimeter="^"ansi_prefix orange_color"---$"
  block_delimeter="^"ansi_prefix orange_color"---"reset_color

  add_pattern=ansi_prefix"(7;)?[0-9]+;34m"
  delete_pattern=ansi_prefix"(7;)?[0-9]+;31m"
  reset_total_mod()
  total_add_pattern="("add_pattern"|"delete_pattern")([^\x1b]*)"reset_color""
  total_add_pattern_2nd_file="^ +"total_add_pattern
  total_add_pattern_1st_file="^"total_add_pattern

  begin_output=0
  start_pattern="This text explains"
  # https://stackoverflow.com/a/14064658/21294350
  x = SUBSEP
  # These lines are skipped
  skip_line_pattern_str="“mcs”" \
    x all_color"([0-9]+| |\\([0-9\\.]+\\))"reset_color # skip exact number / single space / (num_idx). At least until 'Problem 4.12', they have no unnecessary filters.
  find_weird_ctrl_L=0
  skip_patterns[0]=""
  split(skip_line_pattern_str, skip_patterns, x)
  print skip_patterns[1]
  block=""
  problem_pattern="^ *"all_color"?((Exam|Homework|Class|Practice) )?Problem(s| [0-9])"
  find_problem=0
  find_ansi=0

  skip_ctrl_L=1
  limit_ctrl_L_skip=1
  skip_ctrl_L_cnt=0
  skip_ctrl_L_contents=""
  # when skip_cnt=1, it occasionally skips all total_mod lines for mcs.pdf file comparison.
  skip_cnt=1

  # logging
  log_filter=0
  log_skip=0
  if (skip_ctrl_L) {
    log_ctrl_L=0
  } else{
    log_ctrl_L=0
  }
  log_total_mod=1
}
{
  if (match($0, start_pattern)) {
    print "begin_output"
    begin_output=1
  }
  if (!begin_output) {
    next # only called at the beginning once.
  }
  for (Index = 1; Index <= length(skip_patterns); Index++) {
    if (match($0, skip_patterns[Index])) {
      if (log_skip) {
        # 1. . ~/.virtualenv/misc/bin/activate;icdiff mcs-unlocked.txt mcs_2018-unlocked.txt | awk -f diff_pdf_text.awk | less_n | grep -v 'page ' | less_n
        # probably means “mcs” doesn't filter anything unnecessarily.
        print "find skip_patterns:" skip_patterns[Index] ":in "$0";" 
      }
      next
    }
  }
  if (match($0, problem_pattern)) {
    # print "find problem_pattern:" $0
    find_problem=1
  }
  # ^L is FF https://www.gnu.org/software/gawk/manual/html_node/Escape-Sequences.html
  # To avoid skip '7.6 Search Trees'.
  if (skip_ctrl_L) {
    if (match($0, "^ *"all_color"\x0c")) {
      if (log_ctrl_L) {
        print "find ^L in:"$0";" 
      }
      find_weird_ctrl_L=1
      if (limit_ctrl_L_skip) {
        skip_ctrl_L_contents=$0
        if (log_ctrl_L) {
          print "skip_ctrl_L_contents reset to ^L:"$0";"
        }
      }
      next
    }
    if (find_weird_ctrl_L) {
      if (match($0, "^ *"all_color)) {
        if (skip_ctrl_L_cnt<skip_cnt) {
          if (log_ctrl_L) {
            # At least until Chapter 5
            # Only skips something like 'Chapter 5 Induction' or '5.3. Strong Induction vs. Induction vs. Well Ordering'
            print "skip due to ^L in:"$0";"
          }
          if (limit_ctrl_L_skip) {
            skip_ctrl_L_cnt+=1
            skip_ctrl_L_contents=skip_ctrl_L_contents"\n"$0
            if (log_ctrl_L) {
              print "skip_ctrl_L_contents becomes:"skip_ctrl_L_contents\
                ";skip_ctrl_L_contents becomes end"
            }
          }
          next # notice this may skipped one block.
        } else if (skip_ctrl_L_cnt == skip_cnt) {
          block=block"\n"skip_ctrl_L_contents
          find_ansi+=skip_cnt+1 # include ^L
          # in the above process, 
          # 1. "block_delimeter" is impossible
          # 2. total_mod is implicitly checked
          skip_ctrl_L_cnt+=1
        }
        # when skip_ctrl_L_cnt>skip_cnt, we let the following manipulate.
      } else {
        find_weird_ctrl_L=0
        skip_ctrl_L_cnt=0
        # block,find_ansi will be reset when going into the next block.
      }
    }
  }

  if (match($0, block_delimeter)) {
    if (find_ansi && !find_problem) {
      print block 
    } else if (log_filter) {
      print "no diff found after filter with (find_ansi,find_problem):("\
         find_ansi "," find_problem ")"
      if (!find_ansi) {
        # until '32 \n\n.... Chapter 2 The Well Ordering Principle' all skipped contents have no color highlighted contents
        print "find_ansi=0 -> skip\n" block "\nskip end" 
      }
      if (find_problem) {
        # until 'Problem 2.1.' no unnecessary filters.
        print "find_problem=1 -> skip\n" block "\nskip end" 
      }
    }
    # print "new block"
    block=$0
    find_ansi=0
    find_problem=0
    reset_total_mod()
    next # only skip duplicate `block_delimeter` in `block`
  }

  # 1. Put after block_delimeter to exclude matching '---'
  # 2. use `^(\x1b\[(7;)?[0-9]+;34m|\x1b\[(7;)?[0-9]+;34m)(.*)...$` in regex101
  # `^(\[(7;)?[0-9]+;31m|\[(7;)?[0-9]+;34m)(.*)\[m` with esc removed
  # 3. Here only one of 2 blocks is allowed to run for one line.
  #############################
  # Since the order may be in chaos, e.g.
  # a
  #   b
  #   c
  #   a
  # c
  # b
  # Here I only check the 1st pair (a,a) of 3.
  #############################
  if (total_mod!="") {
    if (find_total_add_file_idx==1) {
      match($0, total_add_pattern_2nd_file,a)
    } else if (find_total_add_file_idx==2) {
      match($0, total_add_pattern_1st_file,a)
    }
    if (a[4]==total_mod) {
      if (log_total_mod) {
        print "find matching total_mod:" a[4] ";with line:" $0
      }
      reset_total_mod()
      find_ansi-=2 
      fflush("/dev/stdout")
    }
  } else {
    if (match($0, total_add_pattern_1st_file,a)) {
      find_total_add_file_idx=1
    } else if (match($0, total_add_pattern_2nd_file,a)){
      find_total_add_file_idx=2
    }
    if (find_total_add_file_idx) {
      total_mod=a[4]
      if (log_total_mod) {
        print "find total_mod:" total_mod ";with line:" $0 \
        ";idx:" find_total_add_file_idx 
      }
    }
  }
  if (match($0, all_color)) {
    # print "find ansi_prefix:" $0
    find_ansi+=1
  }
  block=block"\n"$0
  # print "ansi_cnt:" find_ansi
}