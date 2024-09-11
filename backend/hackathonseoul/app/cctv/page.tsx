import { title } from "@/components/primitives";
import Videostream from "@/components/videoStream";

export default function CCTVPage() {
  return (
    <div>
      <h1 className={title()}>Realtime CCTV</h1>
      <Videostream />
    </div>
  );
}
