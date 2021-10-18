import bs4


html1 = "<p><span style = 'text-decoration: underline; color: #3366ff;'>Title:</span >Info</p ><p ><span style = 'color: #3366ff;' ><span style = 'text-decoration: underline;' >Title2:</span ></span >Info2</p >"

soup1 = bs4.BeautifulSoup(html1,'html5lib')
#soup1 = bs4.BeautifulSoup(htm1, 'html.parser')
for match in soup1.findAll(['span','html','p','head','body']):
    match.unwrap()
print(soup1)

