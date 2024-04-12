using System;
using System.Drawing;
using System.Windows.Forms;

namespace HandWriteRecognize
{
    public partial class Form1 : Form
    {
        private bool isDrawing = false;
        private Point previousPoint;

        public Form1()
        {
            InitializeComponent();

            this.BackColor = Color.White;

            this.WindowState = FormWindowState.Maximized;
            this.FormBorderStyle = FormBorderStyle.None;

            this.MouseDown += panel1_MouseDown; 
            this.MouseMove += panel1_MouseMove;
            this.MouseUp += panel1_MouseUp;

            this.KeyDown += (o, e) =>
            {
                if (e.KeyCode == Keys.Escape)
                {
                    Application.Exit();
                }
            };
        }

        private void panel1_MouseDown(object sender, MouseEventArgs e)
        {
            isDrawing = true;
            previousPoint = e.Location;
        }

        private void panel1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isDrawing)
            {
                using (Graphics g = this.CreateGraphics())
                {
                    g.DrawLine(Pens.Black, previousPoint, e.Location);
                    previousPoint = e.Location;
                }
            }
        }

        private void panel1_MouseUp(object sender, MouseEventArgs e)
        {
            isDrawing = false;
        }
    }
}
