authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(',')


check = []
for i in author_names:
  x = i.split(' ')
  check.append(x)
print(check)

author_last_names= []
for i in check:
  author_last_names.append(i[-1])
print(author_last_names)


#We are using join and strip methods in the code below

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped= []
for i in love_maybe_lines:
  love_maybe_lines_stripped.append(i.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)



dirty_harry = "Go ahead, make my day."
split_hairs = dirty_harry.split("a")

print(split_hairs)
