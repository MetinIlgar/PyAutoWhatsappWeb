<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/MetinIlgar/PyAutoWhatsappWeb-Pre-Alpha">
    <img src="/Images/banner.png" alt="Logo">
  </a>

  <h3 align="center">PyAutoWhatsappWeb</h3>

  <p align="center">
    Send multiple or single whatsapp messages at a specific time.
    <br />
    <a href="https://github.com/MetinIlgar/PyAutoWhatsappWeb-Pre-Alpha"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/MetinIlgar/PyAutoWhatsappWeb-Pre-Alpha">View Demo</a>
    ·
    <a href="https://github.com/MetinIlgar/PyAutoWhatsappWeb-Pre-Alpha/issues">Report Bug</a>
    ·
    <a href="https://github.com/MetinIlgar/PyAutoWhatsappWeb-Pre-Alpha/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
	<summary><h2 style="display: inline-block">Table of Contents</h2></summary>
	<ol>
		<li>
			<a href="#about-the-project">About The Project</a>
			<ul>
				<li><a href="#built-with">Built With</a></li>
			</ul>
		</li>
		<li>
			<a href="#getting-started">Getting Started</a>
			<ul>
				<li><a href="#required-libraries">Required Libraries</a></li>
				<li><a href="#installation">Installation</a></li>
			</ul>
		</li>
		<li>
			<a href="#usage">Usage</a>
			<ul>
				<li><a href="#import-phone-numbers">Import Phone Numbers</a></li>
			</ul>
		</li>
		<li><a href="#roadmap">Roadmap</a></li>
		<li><a href="#contributing">Contributing</a></li>
		<li><a href="#license">License</a></li>
		<li><a href="#authors">Authors</a></li>
	</ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Anyone can send single or group messages from Whatsapp. However, you cannot set the timer according to each country's time zone and easily send the message you want at the time you want.

With this program, you can import phone numbers, edit the phone numbers list and send your message at the specified time. It doesn't matter which country you ship to.

Here are the reasons why you should use this program:
* You can send single or multiple messages at any time. 
* Thanks to the timer you set, you can send messages in each country's own time zone. 
* For example, the message you send at 10:00 will be sent to the person in America, to the person in England, to the person in Turkey when the time zone in that country reaches 10:00.

You can suggest changes by forking this repository and creating a pull request or opening an issue.

### Built With

* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Phonenumbers](https://pypi.org/project/phonenumbers/)
* [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
* [Pytz](https://pypi.org/project/pytz/)
* [Colorama](https://pypi.org/project/colorama/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Required Libraries

Type this command in the console to install the required libraries:
* [pip](https://pypi.org/project/pip/)
  ```sh
  $ pip install -r requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MetinIlgar/PyAutoWhatsappWeb-Pre-Alpha.git
   ```
2. Run the software
   ```sh
   python PyAutoWp.py 
   ```


<!-- USAGE EXAMPLES -->
## Usage

### Import phone numbers
To send multiple messages, you need to import phone numbers. You can do this in 2 ways:
1. From Excel file.
2. From the vCard file you imported from the sim card.

* You can edit the given excel file according to your own phone number as in the table example below.

![Sample Excel Spreadsheet](/Images/Sample_Phone_Number_Data_SS.PNG)

* Or, using a vCard with the ".vcf" file extension, convert your phone numbers to an excel file and import them in a format that the program can use.



<!-- ROADMAP -->
## Roadmap

* See the [open issues](https://github.com/MetinIlgar/PyAutoWhatsappWeb-Pre-Alpha/issues) for a list of proposed features (and known issues).

* Take a look at the [commits](https://github.com/MetinIlgar/PyAutoWhatsappWeb-Pre-Alpha/commits/main) to see the build stages of the program.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](https://github.com/MetinIlgar/PyAutoWhatsappWeb/blob/main/LICENSE) for more information.


<!-- CONTACT -->
## Authors

* Metin Ilgar Mutlu

[![GitHub Logo](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MetinIlgar)
![Instagram Logo](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white) 
![Twitter Logo](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white) 








