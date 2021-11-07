<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />

<p align="center">


  <h3 align="center">Myntra Repurpose - Recommendation Engine</h3>

  <p align="center">
    An awesome website to make online thrifting market organized and mainstream. Made with Love.
    <br />
    <a href="https://github.com/FAST-ASDA/recommendation-repurpose"><strong>Explore the docs »</strong></a>
    <br />
    ·
    <a href="https://github.com/FAST-ASDA/recommendation-repurpose/issues">Report Bug</a>
    ·
    <a href="https://github.com/FAST-ASDA/recommendation-repurpose/issues">Request Feature</a>
  </p>
</p>

  
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-engine">About The Engine</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <!-- <li><a href="#prerequisites">Prerequisites</a></li> -->
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <!-- <li><a href="#issues">Issues</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgements">Acknowledgements</a></li> -->
  </ol>
</details>

<!-- ABOUT THE ENGINE -->

## About The Engine

Since we do not have a lot of user interactions, we have built a clustering based recommendation engine using K-Means algorithm. The engine makes a cluster of similar items and recommends product which belong to the similar cluster.


### Built With

- [Python](https://www.python.org)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Pandas](https://pandas.pydata.org/)
- [Sklearn](https://scikit-learn.org/stable/whats_new/v0.22.html)
- [NumPy](https://www.numpy.org/)
- [Scikit-image](https://scikit-image.org/)
- [Amazon Fashion Dataset](https://nijianmo.github.io/amazon/index.html)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.



### Installation

1. Clone the repo
   ```
   $ git clone https://github.com/FAST-ASDA/recommendation-repurpose.git
   $ cd recommendation-repurpose
   ```
2. Activating virtual environment (optional)
   ```
   $ python -m venv venv
   $ venv\Scripts\activate
   ```
3. Install requirements
   ```
   $ pip install -r requirements.txt
   ```
4. Run Application

   ```
   $ python app.py
   ```


<!-- USAGE EXAMPLES -->

## Usage

To get recommendations, you can send your product desciption/title as a query parameter.

  ```
  https://recommendation-repurpose.herokuapp.com/getrecommendation?title=?   
  ```

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
<a href="https://github.com/FAST-ASDA/recommendation-repurpose//blob/master/CONTRIBUTING.md">Read our contributing guidelines</a>


<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

- [Anikash Chakraborty](https://www.linkedin.com/in/anikash-chakraborty/) 
- [Shiva Gupta](https://www.linkedin.com/in/shiva-gupta-1843b6170/) 
- [Divyansh Goel](https://www.linkedin.com/in/divyansh-goel-a0a433166/) 
- [Akshat Tiwari](https://www.linkedin.com/in/akshaaatt/)

<!-- ACKNOWLEDGEMENTS

## Acknowledgements

- [Img Shields](https://shields.io)
- [CASIA 2.0 Dataset](https://github.com/namtpham/casia2groundtruth)
- [MIT License](https://spdx.org/licenses/MIT.html)
- [Anfederico](https://github.com/anfederico/flaskex)
- [Font Awesome](https://fontawesome.com)
- [OBS Studio](https://obsproject.com)
- [Kaggle](https://www.kaggle.com/) -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/killer4639/sach-ka-saamna.svg?style=for-the-badge
[contributors-url]: https://github.com/killer4639/sach-ka-saamna/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/killer4639/sach-ka-saamna.svg?style=for-the-badge
[forks-url]: https://github.com/killer4639/sach-ka-saamna/network/members
[stars-shield]: https://img.shields.io/github/stars/killer4639/sach-ka-saamna.svg?style=for-the-badge
[stars-url]: https://github.com/killer4639/sach-ka-saamna/stargazers
[issues-shield]: https://img.shields.io/github/issues/killer4639/sach-ka-saamna.svg?style=for-the-badge
[issues-url]: https://github.com/killer4639/sach-ka-saamna/issues
[license-shield]: https://img.shields.io/github/license/killer4639/sach-ka-saamna.svg?style=for-the-badge
[license-url]: https://github.com/killer4639/sach-ka-saamna/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/shiva-gupta-1843b6170/

