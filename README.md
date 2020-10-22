# Lodestone
Lodestone is proudly developed on Linux
## About
&nbsp;&nbsp;Lodestone was designed with the goal to be an alternative for downloading large amounts of files from the National Cancer Institute's Genomic Data Commons Data Portal (GDC Portal), making it more efficient for researchers to download items en masse without having to use the GDC Portal's repository (e.g. SVS files: see <a href="https://www.leicabiosystems.com/digital-pathology/manage/aperio-imagescope/">Aperio ImageScope</a>). Through Lodestone, you will be able to directly modify your search criteria (AJCC Pathologic Stage, Gender, Race, File Extension), create corresponding .TSVs, and download any related files that you would want. In order to accomplish this, Lodestone utilizes the <a href="https://gdc.cancer.gov/access-data/gdc-data-transfer-tool">GDC Data Transfer Tool</a> along with Python source code. The GDC Data Transfer Tool allows for efficient download speeds, whereas Python allows for a streamlined and easy-to-modify codebase.<br /><br />

## Prerequisites
### Software
&nbsp;&nbsp;<b>Python 3</b> You can download Python <a href="https://www.python.org/downloads/">here</a>.<br />

&nbsp;&nbsp;You can check which version of python you have on OSX (Mac) or Linux by typing `python --version` or `python3 --version` into a terminal.
Windows does not come with Python out of the box therefore you will have to manually install it.<br />

### Hardware
&nbsp;&nbsp;It is worth noting that many files in the GDC Portal's repository are quite large. Quality internet connection and bandwidth are recommended. Furthermore, Lodestone is a relatively hefty program and performance on older systems may be inconsistent if not nonexistent.

## Platform Support
<table border = "0">
          <tr>
            <th>OS</th>
            <th>Support</th>
            <th>Versions Tested</th>
         </tr>
         <tr>
           <td>Windows</td>
           <td>Yes</td>
           <td>Windows 10</td>
         </tr>
          <tr>
           <td>macOS</td>
           <td>Yes</td>
           <td>Untested</td>
         </tr>
        <tr>
           <td>Linux</td>
           <td>Yes</td>
           <td>Pop!_OS 20.04 LTS<br />Arch Linux</td>
         </tr>
</table>

## Installation Instructions
Note: Lodestone releases do not include binary executables. The main idea behind releases is to mainstream the process of launching the software as opposed to cloning the repo and running the code from terminal.
Download the appropriate release (Lodestone zip archive) from https://github.com/rleboeu/lodestone/releases. 
For Windows users only: Double-click Run.BAT (Windows Batch File). This will spawn a GUI window and a terminal. <br/>
Do not close the terminal unless you want to cancel the download.
