import { render, screen, waitFor, within } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

import { AnalystWorkspace } from "@/components/workspace/analyst-workspace";

describe("AnalystWorkspace", () => {
  it("renders the three primary panels", async () => {
    render(<AnalystWorkspace />);

    await waitFor(() => {
      expect(screen.getByText("Firebase Storage Explorer")).toBeInTheDocument();
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
    await waitFor(() => expect(screen.getByText("Firebase Storage Explorer")).toBeInTheDocument());

    expect(screen.getByLabelText("Open left panel")).toBeInTheDocument();
    expect(screen.getByLabelText("Open right panel")).toBeInTheDocument();
  });

  it("uploads a file into the selected repository folder", async () => {
    const user = userEvent.setup();
    const { container } = render(<AnalystWorkspace />);
    await waitFor(() => expect(screen.getByText("Firebase Storage Explorer")).toBeInTheDocument());

    const tree = screen.getByTestId("repository-folder-tree");
    await user.click(within(tree).getByRole("button", { name: "Reports" }));

    const uploadInput = container.querySelector('input[type="file"]');
    expect(uploadInput).not.toBeNull();
    await user.upload(uploadInput as HTMLInputElement, new File(["fixture"], "hpg-amended.pdf", { type: "application/pdf" }));

    await waitFor(() => {
      expect(screen.getByText(/Uploaded: Reports\/hpg-amended\.pdf/i)).toBeInTheDocument();
    });
  });
});
