#! /bin/awk -f
# See py version for input file generation
# Run `icdiff mcs-unlocked.txt mcs_2018-unlocked.txt | awk -f diff_pdf_text.awk | less_n`.
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

  begin_output=0
  start_pattern="This text explains"
  # https://stackoverflow.com/a/14064658/21294350
  x = SUBSEP
  # These lines are skipped
  skip_pattern_str="“mcs”" \
    x all_color"([0-9]+| |\\([0-9\\.]+\\))"reset_color \
    x "^ *" all_color "?((Exam|Homework|Class|Practice) )?Problems"
  find_weird_ctrl_L=0
  skip_patterns[0]=""
  split(skip_pattern_str, skip_patterns, x)
  print skip_patterns[1]
  block=""
  problem_pattern="Problem [0-9]"
  find_problem=0
  find_ansi=0
}
{
  if (match($0, start_pattern)) {
    print "begin_output"
    begin_output=1
  }
  if (!begin_output) {
    next
  }
  for (Index = 1; Index <= length(skip_patterns); Index++) {
    if (match($0, skip_patterns[Index])) {
      # print "find skip_patterns:" skip_patterns[Index] ":in "$0";"
      next
    }
  }
  # ^L is FF https://www.gnu.org/software/gawk/manual/html_node/Escape-Sequences.html
  if (match($0, "^ *"all_color"\x0c")) {
    # print "find ^L in:"$0";"
    find_weird_ctrl_L=1
    next
  }
  if (find_weird_ctrl_L) {
    if (match($0, "^ *"all_color)) {
      # print "skip due to ^L in:"$0";"
      next 
    } else{
      find_weird_ctrl_L=0
    }
  }
  if (match($0, block_delimeter)) {
    if (find_ansi && !find_problem) {
      print block 
    } else{
      print "no diff found after filter"
    }
    print "new block"
    block=$0
    find_ansi=0
    find_problem=0
    next
    print "block_delimeter:" $0
  }
  if (match($0, "^ *"all_color"?"problem_pattern)) {
    # print "find problem_pattern:" $0
    find_problem=1
  }
  if (match($0, all_color)) {
    # print "find ansi_prefix:" $0
    find_ansi=1
  }
  block=block"\n"$0
}