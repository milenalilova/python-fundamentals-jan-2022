title = input()
print(f"<h1>\n    {title}\n</h1>")

content = input()
print(f"<article>\n    {content}\n</article>")

comment = input()
while comment != "end of comments":
    print(f"<div>\n    {comment}\n</div>")
    comment = input()


# Variant 2

# title = input()
# content = input()
# print(f"""
# <h1>
# {title}
# </h1>
# <article>
# {content}
# </article>
# """, end='')
# comment = input()
# while comment != "end of comments":
#     print('<div>')
#     print(comment)
#     print('</div>')
#     comment = input()