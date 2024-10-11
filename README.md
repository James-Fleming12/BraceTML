A compiler for an updated (probably worse) HTML syntax (`.btml`)
```btml
header {
    title { My Title }
}
body {
    h1 {
        Hello World
    }
}
```
should compile to the following
```html
<!DOCTYPE html>
<head>
    <title>My Title</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
```


## To Be Implemented:
- [ ] Basic Markup
- [ ] Classes and IDs
- [ ] Stylings (under `!!!STYLE`)