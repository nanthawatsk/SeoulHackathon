import UploadVideo from "@/components/videoUpload";
export default async function Home() {
  return (
    <div>
      <h1 className="text-4xl font-bold text-center">Welcome to Accident CCTV Detection System</h1>
      <UploadVideo />
    </div>
  );
}
