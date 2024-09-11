"use client";
import { useState, ChangeEvent } from "react";
import { Button } from "@nextui-org/react";
import Alert from '@mui/material/Alert';
import Collapse from '@mui/material/Collapse';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';

export default function UploadVideo() {
  const [videoFile, setVideoFile] = useState<File | null>(null);
  const [videoPreview, setVideoPreview] = useState<string | null>(null);
  const [alertMessage, setAlertMessage] = useState<string | null>(null);
  const [showAlert, setShowAlert] = useState<boolean>(false);
  const [alertSeverity, setAlertSeverity] = useState<'success' | 'error'>('success');
  const [loading, setLoading] = useState<boolean>(false); // Loading state

  // Handle file selection and preview
  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      if (videoPreview) {
        URL.revokeObjectURL(videoPreview); // Free memory used by previous preview
        setVideoPreview(null);
      }
      setVideoFile(file);
      setTimeout(() => {
        setVideoPreview(URL.createObjectURL(file)); // Preview newly selected video
      }, 0);
    }
  };

  // Handle file upload to backend
  const handleFileUpload = async () => {
    if (!videoFile) {
      setAlertMessage("Please select a video file.");
      setAlertSeverity("error");
      setShowAlert(true);
      return;
    }

    const formData = new FormData();
    formData.append("video", videoFile);

    setLoading(true); // Start loading

    try {
      const res = await fetch("http://localhost:5002/process_video", {
        method: "POST",
        body: formData,
        mode: "cors",
      });

      if (res.ok) {
        setAlertMessage("Video analysis completed successfully.");
        setAlertSeverity("success");
      } else {
        setAlertMessage("Failed to upload video.");
        setAlertSeverity("error");
      }
      setShowAlert(true);
    } catch (error) {
      setAlertMessage("Error uploading video.");
      setAlertSeverity("error");
      setShowAlert(true);
    } finally {
      setLoading(false); // Stop loading
    }
  };

  return (
    <div className="text-center mt-4">
      <h2 className="text-2xl font-bold">Upload and Display Video</h2>

      {/* File input */}
      <input className="mt-4" type="file" accept="video/*" onChange={handleFileChange} />

      {/* Video preview */}
      {videoPreview && (
        <div className="flex justify-center mt-4">
          <video width="540" controls>
            <source src={videoPreview} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      )}

      {/* Upload button */}
      <div className="mt-4">
        <Button color="primary" onClick={handleFileUpload} disabled={loading} isLoading={loading}>
          {loading ? "Analysing..." : "Upload Video"}
        </Button>
      </div>

      {/* Alert for upload status */}
      <div className="mt-4">
        <Collapse in={showAlert}>
          <Alert
            severity={alertSeverity}
            action={
              <IconButton
                aria-label="close"
                color="inherit"
                size="small"
                onClick={() => {
                  setShowAlert(false);
                }}
              >
                <CloseIcon fontSize="inherit" />
              </IconButton>
            }
          >
            {alertMessage}
          </Alert>
        </Collapse>
      </div>
    </div>
  );
}
