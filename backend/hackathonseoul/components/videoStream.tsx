export default function VideoStream() {
    return (
        <div>
        <div className="video-container mt-4">
            <img
                src="http://kamera.mikulov.cz:8888/mjpg/video.mjpg"
                alt="Video Stream"
                style={{ width: '100%', height: 'auto' }}
            />
        </div>
    </div>    
    );
    }