using System.Drawing;
using System.Windows.Forms;
using System;
using Timer = System.Windows.Forms.Timer;
using System.Diagnostics;

namespace HandWriteRecognize
{
    public partial class Form1 : Form
    {
        PictureBox pb = new PictureBox();
        Bitmap bmp;
        Timer tm;
        Graphics g;
        string uploadedImagePath = "";
        private bool isDrawing = false;
        private Point previousPoint;
        private int thickness = 5;
        private bool isErasing = false;
        public Button createButton(string text, Point point, Size size)
        {
            Button button = new Button();
            button.Text = text;
            button.Location = point;
            button.Size = size;
            return button;
        }

        public Form1()
        {
            InitializeComponent();

            Button button = createButton("Fazer upload", new Point(10, 70), new Size(100, 30));
            button.Click += btnSelectImageClick;
            this.Controls.Add(button);

            Button button2 = createButton("Fazer leitura\nda imagem", new Point(10, 100), new Size(100, 40));
            // button2.Click += ;
            this.Controls.Add(button2);

            this.KeyPreview = true;

            this.tm = new Timer();
            this.tm.Interval = 20;

            this.BackColor = Color.White;

            this.WindowState = FormWindowState.Maximized;
            this.FormBorderStyle = FormBorderStyle.None;

            this.Controls.Add(pb);
            pb.Dock = DockStyle.Fill;

            pb.MouseDown += pb_MouseDown;
            pb.MouseMove += pb_MouseMove;
            pb.MouseUp += pb_MouseUp;

            this.KeyDown += (o, e) =>
            {
                if (e.KeyCode == Keys.Escape)
                    Application.Exit();

                if (e.KeyCode == Keys.Back)
                    clearPanel();

                if (e.KeyCode == Keys.E)
                    isErasing = !isErasing;
            };

            this.MouseWheel += (o, e) =>
            {
                if (e.Delta > 0)
                    this.thickness++;
                else
                {
                    if (this.thickness > 1)
                    {
                        this.thickness--;
                    }
                }
            };

            this.Load += (o, e) =>
            {
                this.bmp = new Bitmap(pb.Width, pb.Height);
                g = Graphics.FromImage(bmp);
                g.Clear(Color.White);
                this.pb.Image = bmp;
            };

            tm.Tick += (o, e) =>
            {
                Frame();
                pb.Refresh();
            };
            tm.Start();
        }

        void Frame()
        {
            string thicknessText = $"{thickness}";
            Font thicknessFont = new Font("Arial", 12);
            Brush thicknessBrush = Brushes.Black;
            PointF thicknessPoint = new PointF(10, 10);
            g.FillRectangle(Brushes.GhostWhite, thicknessPoint.X, thicknessPoint.Y, 30, 20);
            g.DrawString(thicknessText, thicknessFont, thicknessBrush, thicknessPoint);

            string commandsText = "E = Erase\nBackSpace = Clear";
            Font commandsFont = new Font("Arial", 12);
            Brush commandsBrush = Brushes.Black;
            PointF commandsPoint = new PointF(10, 30);
            g.FillRectangle(Brushes.GhostWhite, commandsPoint.X, commandsPoint.Y, 200, 40);
            g.DrawString(commandsText, commandsFont, commandsBrush, commandsPoint);

            var splitText = uploadedImagePath.Split('\\');
            string file = splitText[splitText.Length - 1];
            Font fileFont = new Font("Arial", 12);
            Brush fileBrush = Brushes.Black;
            PointF filePoint = new PointF(110, 110);
            g.FillRectangle(Brushes.GhostWhite, filePoint.X, filePoint.Y, 200, 40);
            g.DrawString(file, fileFont, fileBrush, filePoint);
        }

        private void clearPanel()
        {
            g.Clear(Color.White);
            pb.Invalidate();
        }
        private void pb_MouseDown(object sender, MouseEventArgs e)
        {
            isDrawing = true;
            previousPoint = e.Location;
        }

        private void pb_MouseUp(object sender, MouseEventArgs e)
        {
            isDrawing = false;
        }
        private void pb_MouseMove(object sender, MouseEventArgs e)
        {
            if (isDrawing)
            {
                Brush brush = isErasing ? Brushes.White : Brushes.Black;
                var deltaX = e.X - previousPoint.X;
                var deltaY = e.Y - previousPoint.Y;
                var dist = MathF.Sqrt(deltaX * deltaX + deltaY * deltaY);
                for (float d = 0; d < 1; d += 1f / dist)
                {
                    var x = (1 - d) * previousPoint.X + d * e.X;
                    var y = (1 - d) * previousPoint.Y + d * e.Y;
                    g.FillEllipse(brush,
                        x - thickness / 2,
                        y - thickness / 2,
                        thickness, thickness
                    );
                }
                previousPoint = e.Location;
                pb.Invalidate();
            }

        }

        private void btnSelectImageClick(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog
            {
                Filter = "Arquivos de imagem|*.jpg;*.jpeg;*.png;*.gif;*.bmp|Todos os arquivos|*.*"
            };

            DialogResult result = openFileDialog.ShowDialog();

            if (result == DialogResult.OK)
            {
                try
                {
                    uploadedImagePath = openFileDialog.FileName;
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Ocorreu um erro ao carregar a imagem: " + ex.Message, "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }
    }

}
