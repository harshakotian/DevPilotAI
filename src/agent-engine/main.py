from devpilot.graph.workflow import build_workflow


def main():
    workflow = build_workflow()

    initial_state = {
        "requirement": (
            "Add distributed caching to the Product API "
            "using Redis."
        ),
        "status": "new",
    }

    result = workflow.invoke(initial_state)

    print()
    print("Workflow complete")
    print(result)


if __name__ == "__main__":
    main()