cat9k-soar
----------
Application Hosting on the Catalyst 9K, an interface to Splunk Phantom security orchestration, automation and response (SOAR)

![](./documentation/images/code_for_catalyst_logo.png)

This project uses the application hosting feature of the Catalyst 9K as a distributed platform for gathering and pushing security data to Phantom. This data can be combined with other enrichment sources, and as a trigger for automating incident response.

### Technology Value

### Components

**SOAR** Splunk Phantom: Security Orchestration, Automation and Response (SOAR)

**Linux Containers** Docker:

**Application Hosting** Catalyst 9K

### Status

trigger Phantom into action, such as incidents, threat indicators, vulnerabilities, emails, and more. Phantom gives you full access to the contents of your security data for the purposes of automated decision making.
Splunk Phantom Security Orchestration


# Project Title

Put a meaningful, short, plain-language description of what this code is trying to accomplish, what is the business driver for implementation, and in general why it matters. 

Pro tips: 

* Code Exchange displays the first few content lines of your README in the tile it creates for your repo. If you enter a GitHub Description, Code Exchange uses that instead. 
* Code Exchange works best with READMEs formatted in [GitHub's flavor of Markdown](https://guides.github.com/features/mastering-markdown/). Support for reStructuredText is a work in progress.

Other things you might include:

* Technology stack: Indicate the technological nature of the code, including primary programming language(s) and whether the code is intended as standalone or as a module in a framework or other ecosystem.
* Status:  Alpha, Beta, 1.1, etc. It's OK to write a sentence, too. The goal is to let interested people know where what they can expect from this code.
* Screenshot: If the code has visual components, place a screenshot after the description; e.g.,

![add-image-here]()


## Installation

Detailed instructions on how to install, configure, and get the project running. Call out any dependencies. This should be frequently tested and updated to make sure it works reliably, accounts for updated versions of dependencies, etc.

## Configuration

If the code is configurable, describe it in detail, either here or in other documentation that you reference.

## Usage

Show users how to use the code. Be specific.
Use appropriate formatting when showing code snippets or command line output.
If a particular [DevNet Sandbox](https://developer.cisco.com/sandbox/) or [Learning Lab](https://developer.cisco.com/learning-labs/) can be used in to provide a network or other resources to be used with this code, call that out here. 

## How to test the software

Provide details on steps to test, versions of components/depencencies against which code was tested, date the code was last tested, etc. 
If the repo includes automated tests, detail how to run those tests.
If the repo is instrumented with a continuous testing framework, that is even better.

## Known issues

Document any known significant shortcomings with the code. If using the [Issue Tracker](./issues), make that known here and provide any templates or conventions to be followed when opening a new issue. 

## Getting help

Instruct users how to get help with this code; this might include links to an issue tracker, wiki, mailing list, etc.

**Example**

If you have questions, concerns, bug reports, etc., please file an issue in this repository's [Issue Tracker](./issues).

## Getting involved

This section should detail why people should get involved and describe key areas you are currently focusing on; e.g., trying to get feedback on features, fixing certain bugs, building important pieces, etc. Include information on how to setup a development environment if different from general installation instructions.

General instructions on _how_ to contribute should be stated with a link to [CONTRIBUTING](./CONTRIBUTING.md).


----

## Licensing info

A license is required for others to be able to use your code. An open source license is more than just a usage license, it is license to contribute and collaborate on code. Open sourcing code and contributing it to [Code Exchange](https://developer.cisco.com/codeexchange/)  requires a commitment to maintain the code and help the community use and contribute to the code. 

Choosing a license can be difficult and depend on your goals for your code, other licensed code on which your code depends, your business objectives, etc.   This template does not intend to provide legal advise. You should seek legal counsel for that. However, in general, less restrictive licenses make your code easier for others to use.

> Cisco employees can find licensing options and guidance [here](https://wwwin-github.cisco.com/eckelcu/DevNet-Code-Exchange/blob/master/GitHubUsage.md#licensing-guidance).

Once you have determined which license is appropriate, GitHub provides functionality that makes it easy to add a LICENSE file to a GitHub repo, either when creating a new repo or by adding to an existing repo.

When creating a repo through the GitHub UI, you can click on *Add a license* and select from a set of [common open source licenses](https://opensource.org/licenses). See [detailed instructions](https://help.github.com/articles/licensing-a-repository/#applying-a-license-to-a-repository-with-an-existing-license).

Once a repo has been created, you can easily add a LICENSE file through the GitHub UI at any time. Simply select *Create New File*, type *LICENSE* into the filename box, and you will be given the option to select from a set of common open source licenses. See [detailed instructions](https://help.github.com/articles/adding-a-license-to-a-repository/).

Once you have created the LICENSE file, be sure to update/replace any templated fields with appropriate information, including the Copyright. For example, the [3-Clause BSD license template](https://opensource.org/licenses/BSD-3-Clause) has the following copyright notice:

`Copyright (c) <YEAR>, <COPYRIGHT HOLDER>`

See the [LICENSE](./LICENSE) for this template repo as an example.

Once your LICENSE file exists, you can delete this section of the README, or replace the instructions in this section with a statement of which license you selected and a link to your license file, e.g.

This code is licensed under the BSD 3-Clause License. See [LICENSE](./LICENSE) for details.

Some licenses, such as Apache 2.0 and GPL v3, do not include a copyright notice in the [LICENSE](./LICENSE) itself. In such cases, a NOTICE file is a common place to include a copyright notice. For a very simple example, see [NOTICE](./NOTICE). 

In the event you make use of 3rd party code, it is required by some licenses, and a good practice in all cases, to provide attribution for all such 3rd party code in your NOTICE file. For a great example, see [https://github.com/cisco/ChezScheme/blob/master/NOTICE]().   

----

## Credits and references

1. Projects that inspired you
2. Related projects
3. Books, papers, talks, or other sources that have meaningful impact or influence on this code
