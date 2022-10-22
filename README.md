# Notes ++

- dendron template taken from [here](https://github.com/dendronhq/template.publish.github-action/)
- You'll need to change both the siteUrl and assetsPrefix fields in dendron.yml to your own location

## Common markdown snippets

- togglable blocks
<details>
<summary> <b>CODE</b> </summary>

</details>

Unfortunately dendron does not support that in published pages. You can toggle only on your local.

- image

```
![name.png](assets/images/name.png)
```

- [mermaid](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) enabled

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
