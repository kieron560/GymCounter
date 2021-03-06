<!--
*** Thanks for checking out the GymCounter. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** kieron560, GymCounter, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-shield]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Gym Counter Bot</h3>
  <p align="center">
    A basic Telegram Bot that uses webscrapping via Beautiful Soup 4 to get the number of people in the Anytime Fitness Singapore.
    <br />
    <br />
    <br />
    <a href="https://github.com/kieron560/GymCounter">View Demo</a>
    ·
    <a href="https://github.com/kieron560/GymCounter/issues">Report Bug</a>
    ·
    <a href="https://github.com/kieron560/GymCounter/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
        <a href="#built-with">Built With</a></li>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#testing">Testing</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Built With

* [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)
* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Locations Supported
* Anytime Fitness Pasir Ris E!Hub
* Anytime Fitness Sengkang Rivervale
* Anytime Fitness SKH Campus
* Anytime Fitness Pasir Ris Elias CC


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kieron560/GymCounter.git
   ```

2. Install the requirements
   ```sh
   pip install -r requirements.txt
   ```

3. Request for the telegram Bot tokens from me and set the tokens inside `/tester_bot` 
   ```
   cd /tester_bot
   echo 'TESTER_BOT_TOKEN' > test_token.txt

   # replace 'TESTER_BOT_TOKEN' with the actual token 
   ```

### Testing

You will be using the tester_bot to test your features that you have created. It is a replica of the `bot.py` with some changes, so adjust the code accordingly!

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/kieron560/GymCounter/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- CONTACT -->
## Contact

Kieron Koh - kieron560@gmail.com

Project Link: [https://github.com/kieron560/GymCounter](https://github.com/kieron560/GymCounter)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Best-README-template](https://github.com/othneildrew/Best-README-Template)

[contributors-shield]: https://img.shields.io/github/contributors/kieron560/GymCounter.svg?style=for-the-badge
[contributors-url]: https://github.com/kieron560/GymCounter/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kieron560/GymCounter.svg?style=for-the-badge
[forks-url]: https://github.com/kieron560/GymCounter/network/members
[stars-shield]: https://img.shields.io/github/stars/kieron560/GymCounter.svg?style=for-the-badge
[stars-url]: https://github.com/kieron560/GymCounter/stargazers
[issues-shield]: https://img.shields.io/github/issues/kieron560/GymCounter.svg?style=for-the-badge
[issues-url]: https://github.com/kieron560/GymCounter/issues
[license-shield]: https://img.shields.io/github/license/kieron560/GymCounter.svg?style=for-the-badge
[license-url]: https://github.com/kieron560/GymCounter/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/kieron-koh-a29216196/
