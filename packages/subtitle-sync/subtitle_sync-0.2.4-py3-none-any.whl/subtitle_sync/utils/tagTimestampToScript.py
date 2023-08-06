


def tagTimestampToScript(pureScript, scriptWithTimestamp):
    index = 0
    for pageIndex, page in enumerate(pureScript):
        for contentIndex, content in enumerate(page["content"]):
            if "scene_info" in content:
                for sceneIndex, scene in enumerate(content["scene"]):
                    if scene["type"] == "CHARACTER" or scene["type"] == "DUAL_DIALOGUE":

                        testDialogues = ""
                        if scene["type"] == "DUAL_DIALOGUE":
                            testDialogues = [
                                scene["content"]["character1"]["dialogue"],
                                scene["content"]["character2"]["dialogue"],
                            ]
                        else:
                            testDialogues = [scene["content"]["dialogue"]]

                        for line in scriptWithTimestamp:
                            if (
                                any(
                                    [
                                        line["dialogue"]
                                        in " ".join(
                                            list(
                                                filter(
                                                    lambda x: "(" != x[0], testDialogue,
                                                )
                                            )
                                        ).lower()
                                        for testDialogue in testDialogues
                                    ]
                                )
                                and "timestamp" in line
                            ):
                                # isolatedLeftWords = line["dialogue"][0:line["distinct"]["matchIndex"]]
                                # length = len(line["distinct"]["subsDialogue"])
                                # rightSection = line["dialogue"][line["distinct"]["matchIndex"]:line["distinct"]["matchIndex"] + len(line["distinct"]["subsDialogue"]) + 1]

                                # isolatedRightWords = line["dialogue"].replace(rightSection, "").replace(isolatedLeftWords, "")
                                
                                # pureScript[pageIndex]["content"][contentIndex]["scene"][
                                #     sceneIndex
                                # ]["timestamp"] = [line["timestamp"][0] - len(isolatedLeftWords.split(" ")),
                                # line["timestamp"][1] + len(isolatedRightWords.split(" "))]

                                # if "timestamp" in pureScript[pageIndex]["content"][contentIndex]["scene"][sceneIndex]:
                                #     pureScript[pageIndex]["content"][contentIndex]["scene"][
                                #         sceneIndex
                                #     ]["timestamp"] = [pureScript[pageIndex]["content"][contentIndex]["scene"][
                                #         sceneIndex
                                #     ]["timestamp"][0], line["timestamp"][1]]
                                # else:
                                pureScript[pageIndex]["content"][contentIndex]["scene"][
                                    sceneIndex
                                ]["timestampOriginal"] = line["timestamp"]
                                pureScript[pageIndex]["content"][contentIndex]["scene"][
                                    sceneIndex
                                ]["timestamp"] = [line["timestamp"][0], line["timestamp"][1]]
                               
                                """
                                remaining words in the left bumps the start timestamp
                                remaining words in the right bumps the end timestamp
                                """
    return pureScript