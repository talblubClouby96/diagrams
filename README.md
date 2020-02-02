<p align="center">
	<img src="assets/img/diagrams.png"/>
</p>

<h1 align="center">Diagrams</h1>
<p align="center">
    Diagram as Code
</p>

Diagrams lets you to draw the cloud system architectures in Python code.

It was born for prototyping a new system architecture without any design tools. You can also describe or visualize the existing system architecture as well.

> NOTE: It does not control the actual cloud resources like cloudformation or terraform, but just for drawing the system architecutrre.

`Diagram as Code` allows you to track the architecture diagram changes on any version control system (same as source code tracking)

Diagrams currently supports three major cloud providers: `AWS`, `Azure`, `GCP`.

> Let me know if you are using diagram! I'll add you in showcase page. (I'm working on it!) :)

## Getting Started

It uses [Graphviz](https://www.graphviz.org/) to render the diagram, so you need to [install Graphviz](https://graphviz.gitlab.io/download/) to use **diagrams**. After installing graphviz (or already have it), install the **diagrams**.

```shell
$ pip install diagrams
```

You can start with [quick start](https://diagram.mingrammer.com/docs/installattion/#quick-start). And you can find [guides](https://diagram.mingrammer.com/diagram) for more details. 

## Examples

## ContributingF

To contribute to diagram, check out [CONTRIBUTING](CONTRIBUTING.md).

## License

[MIT](LICENSE.md)