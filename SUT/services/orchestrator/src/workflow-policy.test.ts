import { describe, it } from "vitest";

// Gate Block 4: property test của planner đạt. Viết bằng fast-check.
describe("planNextStage", () => {
  describe("bảng workflow", () => {
    it.todo("av_only: item mới → dispatch AV; AV xong → item_done");
    it.todo("av_cdr_dlp: AV + CDR song song, rồi DLP");
    it.todo("av_then_sandbox: AV nghi ngờ → sandbox; AV sạch → item_done");
  });

  describe("thuộc tính", () => {
    it.todo("không bao giờ lên lịch engine ngoài danh sách mong đợi của policy");
    it.todo("không lên lịch một engine hai lần cho cùng attempt");
    it.todo("tất định: cùng (policy, snapshot) luôn cho cùng quyết định");
  });
});
