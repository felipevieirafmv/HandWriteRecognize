using System;
using System.IO;
using System.Windows.Forms;
using HandWriteRecognize;
using System.Threading;
using System.Windows.Forms;

string csv = "./english.csv";

string[] lines = File.ReadAllLines(csv);
string[] cleanLines = new string[lines.Length - 1];
Array.Copy(lines, 1, cleanLines, 0, cleanLines.Length);

foreach (string line in cleanLines)
{
    string[] parts = line.Split(',');
    string imgName = parts[0];
    string character = imgName.Substring(8, 2);

    character = $"Img/{character}/";

    MoveImage(imgName, character);
}
MessageBox.Show("Done");

void MoveImage(string origin, string destiny)
{
    if(!Directory.Exists(destiny))
        Directory.CreateDirectory(destiny);
    File.Move(origin, destiny + Path.GetFileName(origin));
}

// Thread.CurrentThread.SetApartmentState(ApartmentState.Unknown);
// Thread.CurrentThread.SetApartmentState(ApartmentState.STA);

// Application.EnableVisualStyles();
// Application.SetCompatibleTextRenderingDefault(false);

// var form = new Form1();
// Application.Run(form);