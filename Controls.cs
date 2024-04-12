namespace HandWriteRecognize;
public class Controls
{
    private TrackBar trackBar1;
    public float TrackBar1()
    {
        trackBar1 = new TrackBar();
        trackBar1.Minimum = 1;
        trackBar1.Maximum = 10;
        trackBar1.Value = 5;

        
        return trackBar1.Value;
    }

}