import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

import { AnalystWorkspace } from "@/components/workspace/analyst-workspace";

describe("AnalystWorkspace", () => {
  it("renders the three primary panels", async () => {
    render(<AnalystWorkspace />);

    await waitFor(() => {
      expect(screen.getByText("Document tree")).toBeInTheDocument();
    });

    expect(screen.getByText("Evidence-first query thread")).toBeInTheDocument();
    expect(screen.getByText("Snippet stack")).toBeInTheDocument();
  });

  it("runs a query and syncs the selected citation into the preview panel", async () => {
    const user = userEvent.setup();
    render(<AnalystWorkspace />);

    await waitFor(() => expect(screen.getByText("Run query")).toBeInTheDocument());
    await user.click(screen.getByText("Run query"));

    await waitFor(() => expect(screen.getByTestId("answer-card")).toBeInTheDocument());
    await user.click(screen.getByRole("button", { name: /Open citation HPG Annual Report 2024 page 87/i }));

    await waitFor(() => {
      expect(screen.getByTestId("preview-panel")).toHaveTextContent("Preview resolved");
      expect(screen.getByTestId("preview-panel")).toHaveTextContent("Trang 87");
    });
  });

  it("injects a voice draft into the query composer", async () => {
    const user = userEvent.setup();
    render(<AnalystWorkspace />);
    await waitFor(() => expect(screen.getByText("Voice draft")).toBeInTheDocument());

    await user.click(screen.getByText("Voice draft"));

    expect(screen.getByLabelText("Query input")).toHaveValue("Tổng hợp các rủi ro chính của SSI trong báo cáo gần đây");
    expect(screen.getByTestId("current-prompt")).toHaveTextContent("Tổng hợp các rủi ro chính của SSI trong báo cáo gần đây");
  });

  it("shows mobile panel controls", async () => {
    render(<AnalystWorkspace />);
    await waitFor(() => expect(screen.getByText("Document tree")).toBeInTheDocument());

    expect(screen.getByLabelText("Open left panel")).toBeInTheDocument();
    expect(screen.getByLabelText("Open right panel")).toBeInTheDocument();
  });
});
