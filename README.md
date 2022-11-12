# Notes ++

- dendron template taken from [here](https://github.com/dendronhq/template.publish.github-action/)
- You'll need to set your own **siteUrl**, **assetsPrefix**, **ga tracking** fields in `dendron.yml`

## Common markdown snippets

togglable blocks
<details>
<summary> <b>CODE</b> </summary>

</details>


display image

```
![name.png](assets/images/name.png)
```

[mermaid](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) enabled

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
