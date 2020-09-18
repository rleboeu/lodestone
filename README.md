# Lodestone
## About Lodestone
&nbsp;&nbsp;Lodestone was designed with the goal to be an alternative for downloading large amounts of files from the National Cancer Institute's Genomic Data Commons Data Portal (GDC Portal), making it more efficient for researchers to download items en masse without having to use the GDC Portal's repository (e.g. SVS files: see <a href="https://www.leicabiosystems.com/digital-pathology/manage/aperio-imagescope/">Aperio ImageScope</a>). Through Lodestone, you will be able to directly modify your search criteria (AJCC Pathologic Stage, Gender, Race, File Extension), create corresponding .TSVs, and download any related files that you would want. In order to accomplish this, Lodestone utilizes the <a href="https://gdc.cancer.gov/access-data/gdc-data-transfer-tool">GDC Data Transfer Tool</a> along with Python source code. The GDC Data Transfer Tool allows for efficient download speeds, whereas Python allows for a streamlined and easy-to-modify codebase.<br /><br />
&nbsp;&nbsp;Lodestone is developed on Linux (Pop!\_OS and Arch), therefore Linux support will always be available. <b>Official Windows support coming soon!</b>

## Prerequisites
&nbsp;&nbsp;<b>python2.7 or higher</b> (<a href="https://www.python.org/downloads/">python3 recommended</a>).<br />

&nbsp;&nbsp;You can check which version of python you have on OSX (Mac) or Linux by typing `python --version` or `python3 --version` into a terminal.
For Windows, it would be simpler to `right click Start -> Apps and Features -> Programs and Features` and search for the python entry.<br />

&nbsp;&nbsp;It is worth noting that many files in the GDC Portal's repository are quite large. Quality internet connection and bandwidth are recommended. Furthermore, Lodestone is a relatively hefty program, therefore performance on older systems may be inconsistent or nonexistent.

### Officially Supported Operating Systems
<table border = "0">
          <tr>
            <th>OS</th>
            <th>Support</th>
            <th>Versions Tested</th>
         </tr>
         <tr>
           <td>Windows</td>
           <td>No</td>
           <td>----</td>
         </tr>
          <tr>
           <td>OSX/macOS</td>
           <td>Yes</td>
           <td>10.15 Catalina</td>
         </tr>
        <tr>
           <td>Linux</td>
           <td>Yes</td>
           <td>Pop!_OS 20.04 LTS<br />Arch Linux kern. 5.8.5</td>
         </tr>
</table>
## Installation Instructions
## License
