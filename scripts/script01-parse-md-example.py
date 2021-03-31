import frontmatter
import marko

post = frontmatter.load('data/document/food-data-collection-in-consumption-and-expenditure-hhs/index.md')

# Example

print(post.keys())
print('-----------------')
print(post.metadata)
print('-----------------')

print(marko.convert(post.content))