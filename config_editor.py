from PyQt5 import QtCore, QtWidgets

from ctypes import windll


def MessageBox(title, text, icon=0x10):
    windll.user32.MessageBoxW(0, text, title, icon)


class ApplicationMainWindow(QtWidgets.QMainWindow):

    def WindowInit(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QtCore.QSize(800, 0))
        MainWindow.setMaximumSize(QtCore.QSize(800, 1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(0, 0, 796, 41))
        self.MainLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 87 12pt \"Segoe UI Black\";")
        self.MainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MainLabel.setObjectName("MainLabel")
        self.TokenInput = QtWidgets.QLineEdit(self.centralwidget)
        self.TokenInput.setGeometry(QtCore.QRect(20, 70, 361, 31))
        self.TokenInput.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-style: solid;\n"
                                      "border-width: 1;\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "border-radius: 5;\n"
                                      "font: 87 10pt \"Segoe UI Black\";\n"
                                      "padding-left: 5;")
        self.TokenInput.setObjectName("TokenInput")
        self.InputCommandPrefix = QtWidgets.QLineEdit(self.centralwidget)
        self.InputCommandPrefix.setGeometry(QtCore.QRect(250, 110, 131, 31))
        self.InputCommandPrefix.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style: solid;\n"
            "border-width: 1;\n"
            "border-color: rgb(255, 255, 255);\n"
            "border-radius: 5;\n"
            "font: 87 10pt \"Segoe UI Black\";\n"
            "padding-left: 5;")
        self.InputCommandPrefix.setObjectName("InputCommandPrefix")
        self.MainGroup = QtWidgets.QLabel(self.centralwidget)
        self.MainGroup.setGeometry(QtCore.QRect(10, 50, 381, 111))
        self.MainGroup.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-style: solid;\n"
                                     "border-width: 1;\n"
                                     "border-color: rgb(255, 255, 255);\n"
                                     "border-radius: 5;\n"
                                     "font: 87 10pt \"Segoe UI Black\";\n"
                                     "padding-left: 5;")
        self.MainGroup.setText("")
        self.MainGroup.setObjectName("MainGroup")
        self.MainGroupLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainGroupLabel.setGeometry(QtCore.QRect(40, 40, 81, 16))
        self.MainGroupLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 87 10pt \"Segoe UI Black\";\n"
                                          "background-color: rgb(0, 0, 0);\n"
                                          "padding-left: 4")
        self.MainGroupLabel.setObjectName("MainGroupLabel")
        self.TextGroup = QtWidgets.QLabel(self.centralwidget)
        self.TextGroup.setGeometry(QtCore.QRect(10, 190, 381, 346))
        self.TextGroup.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-style: solid;\n"
                                     "border-width: 1;\n"
                                     "border-color: rgb(255, 255, 255);\n"
                                     "border-radius: 5;\n"
                                     "font: 87 10pt \"Segoe UI Black\";\n"
                                     "padding-left: 5;")
        self.TextGroup.setText("")
        self.TextGroup.setObjectName("TextGroup")
        self.TextGroupLabel = QtWidgets.QLabel(self.centralwidget)
        self.TextGroupLabel.setGeometry(QtCore.QRect(40, 180, 51, 16))
        self.TextGroupLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 87 10pt \"Segoe UI Black\";\n"
                                          "background-color: rgb(0, 0, 0);\n"
                                          "padding-left: 4")
        self.TextGroupLabel.setObjectName("TextGroupLabel")
        self.ChannelSpamText = QtWidgets.QLineEdit(self.centralwidget)
        self.ChannelSpamText.setGeometry(QtCore.QRect(20, 210, 211, 31))
        self.ChannelSpamText.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style: solid;\n"
            "border-width: 1;\n"
            "border-color: rgb(255, 255, 255);\n"
            "border-radius: 5;\n"
            "font: 87 10pt \"Segoe UI Black\";\n"
            "padding-left: 5;\n"
            "padding-right: 20;")
        self.ChannelSpamText.setObjectName("ChannelSpamText")
        self.BanReason = QtWidgets.QLineEdit(self.centralwidget)
        self.BanReason.setGeometry(QtCore.QRect(240, 210, 141, 31))
        self.BanReason.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-style: solid;\n"
                                     "border-width: 1;\n"
                                     "border-color: rgb(255, 255, 255);\n"
                                     "border-radius: 5;\n"
                                     "font: 87 10pt \"Segoe UI Black\";\n"
                                     "padding-left: 5;\n"
                                     "padding-right: 20;")
        self.BanReason.setObjectName("BanReason")
        self.NewServerName = QtWidgets.QLineEdit(self.centralwidget)
        self.NewServerName.setGeometry(QtCore.QRect(20, 250, 171, 31))
        self.NewServerName.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-style: solid;\n"
                                         "border-width: 1;\n"
                                         "border-color: rgb(255, 255, 255);\n"
                                         "border-radius: 5;\n"
                                         "font: 87 10pt \"Segoe UI Black\";\n"
                                         "padding-left: 5;\n"
                                         "padding-right: 20;")
        self.NewServerName.setObjectName("NewServerName")
        self.RolesName = QtWidgets.QLineEdit(self.centralwidget)
        self.RolesName.setGeometry(QtCore.QRect(200, 250, 181, 31))
        self.RolesName.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-style: solid;\n"
                                     "border-width: 1;\n"
                                     "border-color: rgb(255, 255, 255);\n"
                                     "border-radius: 5;\n"
                                     "font: 87 10pt \"Segoe UI Black\";\n"
                                     "padding-left: 5;\n"
                                     "padding-right: 20;")
        self.RolesName.setObjectName("RolesName")
        self.DMSpam = QtWidgets.QLineEdit(self.centralwidget)
        self.DMSpam.setGeometry(QtCore.QRect(20, 290, 361, 31))
        self.DMSpam.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "border-style: solid;\n"
                                  "border-width: 1;\n"
                                  "border-color: rgb(255, 255, 255);\n"
                                  "border-radius: 5;\n"
                                  "font: 87 10pt \"Segoe UI Black\";\n"
                                  "padding-left: 5;\n"
                                  "padding-right:20;")
        self.DMSpam.setObjectName("DMSpam")
        self.MessageOnStart = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.MessageOnStart.setGeometry(QtCore.QRect(20, 330, 361, 71))
        self.MessageOnStart.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-style: solid;\n"
                                          "border-width: 1;\n"
                                          "border-color: rgb(255, 255, 255);\n"
                                          "border-radius: 5;\n"
                                          "font: 87 10pt \"Segoe UI Black\";\n"
                                          "padding-left: 3;")
        self.MessageOnStart.setObjectName("MessageOnStart")
        self.EnableMessageOnStart = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableMessageOnStart.setGeometry(QtCore.QRect(360, 375, 20, 20))
        self.EnableMessageOnStart.setText("")
        self.EnableMessageOnStart.setObjectName("EnableMessageOnStart")
        self.EnableDMSpam = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableDMSpam.setGeometry(QtCore.QRect(360, 295, 20, 20))
        self.EnableDMSpam.setText("")
        self.EnableDMSpam.setObjectName("EnableDMSpam")
        self.EnableCDRoles = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableCDRoles.setGeometry(QtCore.QRect(360, 255, 20, 20))
        self.EnableCDRoles.setText("")
        self.EnableCDRoles.setObjectName("EnableCDRoles")
        self.EnableServerRename = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableServerRename.setGeometry(QtCore.QRect(170, 255, 20, 20))
        self.EnableServerRename.setText("")
        self.EnableServerRename.setObjectName("EnableServerRename")
        self.EnableMassban = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableMassban.setGeometry(QtCore.QRect(360, 215, 20, 20))
        self.EnableMassban.setText("")
        self.EnableMassban.setObjectName("EnableMassban")
        self.EnableTotalSpam = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableTotalSpam.setGeometry(QtCore.QRect(210, 215, 20, 20))
        self.EnableTotalSpam.setText("")
        self.EnableTotalSpam.setChecked(False)
        self.EnableTotalSpam.setObjectName("EnableTotalSpam")
        self.OtherGroup = QtWidgets.QLabel(self.centralwidget)
        self.OtherGroup.setGeometry(QtCore.QRect(415, 50, 376, 226))
        self.OtherGroup.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-style: solid;\n"
                                      "border-width: 1;\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "border-radius: 5;\n"
                                      "font: 87 10pt \"Segoe UI Black\";\n"
                                      "padding-left: 5;")
        self.OtherGroup.setText("")
        self.OtherGroup.setObjectName("OtherGroup")
        self.OtherGroupLabel = QtWidgets.QLabel(self.centralwidget)
        self.OtherGroupLabel.setGeometry(QtCore.QRect(445, 40, 135, 16))
        self.OtherGroupLabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "font: 87 10pt \"Segoe UI Black\";\n"
            "background-color: rgb(0, 0, 0);\n"
            "padding-left: 4")
        self.OtherGroupLabel.setObjectName("OtherGroupLabel")
        self.EnableRandomChannelsType = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableRandomChannelsType.setGeometry(QtCore.QRect(
            425, 65, 21, 20))
        self.EnableRandomChannelsType.setStyleSheet("")
        self.EnableRandomChannelsType.setText("")
        self.EnableRandomChannelsType.setObjectName("EnableRandomChannelsType")
        self.EnableRandomChannelsTypeLabel = QtWidgets.QLabel(
            self.centralwidget)
        self.EnableRandomChannelsTypeLabel.setGeometry(
            QtCore.QRect(445, 65, 341, 16))
        self.EnableRandomChannelsTypeLabel.setStyleSheet(
            "font: 87 10pt \"Segoe UI Black\";\n"
            "color: rgb(255, 255, 255);")
        self.EnableRandomChannelsTypeLabel.setObjectName(
            "EnableRandomChannelsTypeLabel")
        self.EnableChannelPurge = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableChannelPurge.setGeometry(QtCore.QRect(425, 85, 21, 20))
        self.EnableChannelPurge.setStyleSheet("")
        self.EnableChannelPurge.setText("")
        self.EnableChannelPurge.setObjectName("EnableChannelPurge")
        self.ChannelPurgeLabel = QtWidgets.QLabel(self.centralwidget)
        self.ChannelPurgeLabel.setGeometry(QtCore.QRect(445, 85, 341, 16))
        self.ChannelPurgeLabel.setStyleSheet(
            "font: 87 10pt \"Segoe UI Black\";\n"
            "color: rgb(255, 255, 255);")
        self.ChannelPurgeLabel.setObjectName("EnableRandomChannelsTypeLabel_2")
        self.EnableEmojiRemover = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableEmojiRemover.setGeometry(QtCore.QRect(425, 105, 21, 20))
        self.EnableEmojiRemover.setStyleSheet("")
        self.EnableEmojiRemover.setText("")
        self.EnableEmojiRemover.setObjectName("EnableEmojiRemover")
        self.RemoveEmojisLabel = QtWidgets.QLabel(self.centralwidget)
        self.RemoveEmojisLabel.setGeometry(QtCore.QRect(445, 105, 341, 16))
        self.RemoveEmojisLabel.setStyleSheet(
            "font: 87 10pt \"Segoe UI Black\";\n"
            "color: rgb(255, 255, 255);")
        self.RemoveEmojisLabel.setObjectName("EnableRandomChannelsTypeLabel_3")
        self.EnableInvitesRemover = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableInvitesRemover.setGeometry(QtCore.QRect(425, 125, 21, 20))
        self.EnableInvitesRemover.setStyleSheet("")
        self.EnableInvitesRemover.setText("")
        self.EnableInvitesRemover.setObjectName("EnableInvitesRemover")
        self.RemoveInvitesLabel = QtWidgets.QLabel(self.centralwidget)
        self.RemoveInvitesLabel.setGeometry(QtCore.QRect(445, 125, 341, 16))
        self.RemoveInvitesLabel.setStyleSheet(
            "font: 87 10pt \"Segoe UI Black\";\n"
            "color: rgb(255, 255, 255);")
        self.RemoveInvitesLabel.setObjectName(
            "EnableRandomChannelsTypeLabel_4")
        self.EnableWebhooksCreator = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableWebhooksCreator.setGeometry(QtCore.QRect(425, 145, 21, 20))
        self.EnableWebhooksCreator.setStyleSheet("")
        self.EnableWebhooksCreator.setText("")
        self.EnableWebhooksCreator.setObjectName("EnableWebhooksCreator")
        self.CreateWebhooksLabel = QtWidgets.QLabel(self.centralwidget)
        self.CreateWebhooksLabel.setGeometry(QtCore.QRect(445, 145, 341, 16))
        self.CreateWebhooksLabel.setStyleSheet(
            "font: 87 10pt \"Segoe UI Black\";\n"
            "color: rgb(255, 255, 255);")
        self.CreateWebhooksLabel.setObjectName(
            "EnableRandomChannelsTypeLabel_5")
        self.EnableWebhooksFlooder = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableWebhooksFlooder.setGeometry(QtCore.QRect(425, 165, 21, 20))
        self.EnableWebhooksFlooder.setStyleSheet("")
        self.EnableWebhooksFlooder.setText("")
        self.EnableWebhooksFlooder.setObjectName("EnableWebhooksFlooder")
        self.SpamWebhooksLabel = QtWidgets.QLabel(self.centralwidget)
        self.SpamWebhooksLabel.setGeometry(QtCore.QRect(445, 165, 341, 16))
        self.SpamWebhooksLabel.setStyleSheet(
            "font: 87 10pt \"Segoe UI Black\";\n"
            "color: rgb(255, 255, 255);")
        self.SpamWebhooksLabel.setObjectName("EnableRandomChannelsTypeLabel_6")
        self.EnableRemoveServerTemplate = QtWidgets.QCheckBox(
            self.centralwidget)
        self.EnableRemoveServerTemplate.setGeometry(
            QtCore.QRect(425, 185, 21, 20))
        self.EnableRemoveServerTemplate.setStyleSheet("")
        self.EnableRemoveServerTemplate.setText("")
        self.EnableRemoveServerTemplate.setObjectName("RemoveServerTemplate")
        self.DeleteTemplateLabel = QtWidgets.QLabel(self.centralwidget)
        self.DeleteTemplateLabel.setGeometry(QtCore.QRect(445, 185, 341, 16))
        self.DeleteTemplateLabel.setStyleSheet(
            "font: 87 10pt \"Segoe UI Black\";\n"
            "color: rgb(255, 255, 255);")
        self.DeleteTemplateLabel.setObjectName(
            "EnableRandomChannelsTypeLabel_7")
        self.EnableChangeServerIcon = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableChangeServerIcon.setGeometry(QtCore.QRect(425, 205, 21, 20))
        self.EnableChangeServerIcon.setStyleSheet("")
        self.EnableChangeServerIcon.setText("")
        self.EnableChangeServerIcon.setObjectName("ChangeServerIcon")
        self.ChangeIconLabel = QtWidgets.QLabel(self.centralwidget)
        self.ChangeIconLabel.setGeometry(QtCore.QRect(445, 205, 341, 16))
        self.ChangeIconLabel.setStyleSheet(
            "font: 87 10pt \"Segoe UI Black\";\n"
            "color: rgb(255, 255, 255);")
        self.ChangeIconLabel.setObjectName("EnableRandomChannelsTypeLabel_8")
        self.NewServerIconFileName = QtWidgets.QLineEdit(self.centralwidget)
        self.NewServerIconFileName.setGeometry(QtCore.QRect(425, 230, 361, 31))
        self.NewServerIconFileName.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style: solid;\n"
            "border-width: 1;\n"
            "border-color: rgb(255, 255, 255);\n"
            "border-radius: 5;\n"
            "font: 87 10pt \"Segoe UI Black\";\n"
            "padding-left: 5;")
        self.NewServerIconFileName.setObjectName("NewServerIconFileName")
        self.AutoLeaveGroup = QtWidgets.QLabel(self.centralwidget)
        self.AutoLeaveGroup.setGeometry(QtCore.QRect(415, 305, 376, 56))
        self.AutoLeaveGroup.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-style: solid;\n"
                                          "border-width: 1;\n"
                                          "border-color: rgb(255, 255, 255);\n"
                                          "border-radius: 5;\n"
                                          "font: 87 10pt \"Segoe UI Black\";\n"
                                          "padding-left: 5;")
        self.AutoLeaveGroup.setText("")
        self.AutoLeaveGroup.setObjectName("AutoLeaveGroup")
        self.AutoLeaveGroupLabel = QtWidgets.QLabel(self.centralwidget)
        self.AutoLeaveGroupLabel.setGeometry(QtCore.QRect(445, 295, 101, 16))
        self.AutoLeaveGroupLabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "font: 87 10pt \"Segoe UI Black\";\n"
            "background-color: rgb(0, 0, 0);\n"
            "padding-left: 4")
        self.AutoLeaveGroupLabel.setObjectName("AutoLeaveGroupLabel")
        self.EnableAutoLeave = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableAutoLeave.setGeometry(QtCore.QRect(425, 322, 21, 20))
        self.EnableAutoLeave.setStyleSheet("")
        self.EnableAutoLeave.setText("")
        self.EnableAutoLeave.setObjectName("EnableAutLeave")
        self.EnableAutoLeaveLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnableAutoLeaveLabel.setGeometry(QtCore.QRect(445, 320, 101, 21))
        self.EnableAutoLeaveLabel.setStyleSheet(
            "font: 87 10pt \"Segoe UI Black\";\n"
            "color: rgb(255, 255, 255);")
        self.EnableAutoLeaveLabel.setObjectName("EnableAutoLeaveLabel")
        self.AutoLeave_LeaveAfter = QtWidgets.QLineEdit(self.centralwidget)
        self.AutoLeave_LeaveAfter.setGeometry(QtCore.QRect(560, 315, 221, 31))
        self.AutoLeave_LeaveAfter.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style: solid;\n"
            "border-width: 1;\n"
            "border-color: rgb(255, 255, 255);\n"
            "border-radius: 5;\n"
            "font: 87 10pt \"Segoe UI Black\";\n"
            "padding-left: 5;")
        self.AutoLeave_LeaveAfter.setObjectName("AutoLeave_LeaveAfter")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 806, 551))
        self.Background.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.ExcludesGroup = QtWidgets.QLabel(self.centralwidget)
        self.ExcludesGroup.setGeometry(QtCore.QRect(415, 385, 376, 111))
        self.ExcludesGroup.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-style: solid;\n"
                                         "border-width: 1;\n"
                                         "border-color: rgb(255, 255, 255);\n"
                                         "border-radius: 5;\n"
                                         "font: 87 10pt \"Segoe UI Black\";\n"
                                         "padding-left: 5;")
        self.ExcludesGroup.setText("")
        self.ExcludesGroup.setObjectName("ExcludesGroup")
        self.ExcludesGroupLabel = QtWidgets.QLabel(self.centralwidget)
        self.ExcludesGroupLabel.setGeometry(QtCore.QRect(445, 375, 101, 16))
        self.ExcludesGroupLabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "font: 87 10pt \"Segoe UI Black\";\n"
            "background-color: rgb(0, 0, 0);\n"
            "padding-left: 4")
        self.ExcludesGroupLabel.setObjectName("ExcludesGroupLabel")
        self.BanExcludes = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.BanExcludes.setGeometry(QtCore.QRect(425, 405, 356, 76))
        self.BanExcludes.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-style: solid;\n"
                                       "border-width: 1;\n"
                                       "border-color: rgb(255, 255, 255);\n"
                                       "border-radius: 5;\n"
                                       "font: 87 10pt \"Segoe UI Black\";\n"
                                       "padding-left: 3;")
        self.BanExcludes.setObjectName("BanExcludes")
        self.SpamWebhooksName = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.SpamWebhooksName.setGeometry(QtCore.QRect(20, 410, 361, 71))
        self.SpamWebhooksName.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style: solid;\n"
            "border-width: 1;\n"
            "border-color: rgb(255, 255, 255);\n"
            "border-radius: 5;\n"
            "font: 87 10pt \"Segoe UI Black\";\n"
            "padding-left: 3;")
        self.SpamWebhooksName.setObjectName("SpamWebhooksName")
        self.CreateConfig = QtWidgets.QPushButton(self.centralwidget)
        self.CreateConfig.setGeometry(QtCore.QRect(415, 510, 376, 26))
        self.CreateConfig.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "color: rgb(0, 0, 0);\n"
            "border-color: rgb(255, 255, 255);\n"
            "border-radius: 5;\n"
            "font: 87 10pt \"Segoe UI Black\";")
        self.CreateConfig.setObjectName("CreateConfig")
        self.NewChannelsName = QtWidgets.QLineEdit(self.centralwidget)
        self.NewChannelsName.setGeometry(QtCore.QRect(20, 490, 361, 31))
        self.NewChannelsName.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style: solid;\n"
            "border-width: 1;\n"
            "border-color: rgb(255, 255, 255);\n"
            "border-radius: 5;\n"
            "font: 87 10pt \"Segoe UI Black\";\n"
            "padding-left: 5;\n"
            "padding-right: 20;")
        self.NewChannelsName.setObjectName("NewChannelsName")
        self.EnableCDChannels = QtWidgets.QCheckBox(self.centralwidget)
        self.EnableCDChannels.setGeometry(QtCore.QRect(360, 495, 20, 20))
        self.EnableCDChannels.setText("")
        self.EnableCDChannels.setObjectName("EnableCDChannels")
        self.Background.raise_()
        self.MainLabel.raise_()
        self.MainGroup.raise_()
        self.TokenInput.raise_()
        self.InputCommandPrefix.raise_()
        self.MainGroupLabel.raise_()
        self.TextGroup.raise_()
        self.TextGroupLabel.raise_()
        self.ChannelSpamText.raise_()
        self.BanReason.raise_()
        self.NewServerName.raise_()
        self.RolesName.raise_()
        self.DMSpam.raise_()
        self.MessageOnStart.raise_()
        self.EnableMessageOnStart.raise_()
        self.EnableCDRoles.raise_()
        self.EnableServerRename.raise_()
        self.EnableMassban.raise_()
        self.EnableTotalSpam.raise_()
        self.OtherGroup.raise_()
        self.OtherGroupLabel.raise_()
        self.EnableRandomChannelsType.raise_()
        self.EnableRandomChannelsTypeLabel.raise_()
        self.EnableChannelPurge.raise_()
        self.ChannelPurgeLabel.raise_()
        self.EnableEmojiRemover.raise_()
        self.RemoveEmojisLabel.raise_()
        self.EnableInvitesRemover.raise_()
        self.RemoveInvitesLabel.raise_()
        self.EnableWebhooksCreator.raise_()
        self.CreateWebhooksLabel.raise_()
        self.EnableWebhooksFlooder.raise_()
        self.SpamWebhooksLabel.raise_()
        self.EnableRemoveServerTemplate.raise_()
        self.DeleteTemplateLabel.raise_()
        self.EnableChangeServerIcon.raise_()
        self.ChangeIconLabel.raise_()
        self.NewServerIconFileName.raise_()
        self.AutoLeaveGroup.raise_()
        self.AutoLeaveGroupLabel.raise_()
        self.EnableAutoLeave.raise_()
        self.EnableAutoLeaveLabel.raise_()
        self.AutoLeave_LeaveAfter.raise_()
        self.ExcludesGroup.raise_()
        self.ExcludesGroupLabel.raise_()
        self.BanExcludes.raise_()
        self.SpamWebhooksName.raise_()
        self.CreateConfig.raise_()
        self.NewChannelsName.raise_()
        self.EnableDMSpam.raise_()
        self.EnableCDChannels.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow",
                       "Discord Server Nuker [BY TheMatriX] - Config Editor"))
        self.MainLabel.setText(_translate("MainWindow",
                                          "Nuker: Config editor"))
        self.TokenInput.setPlaceholderText(
            _translate("MainWindow", "Токен краш-бота"))
        self.InputCommandPrefix.setText(_translate("MainWindow", "!"))
        self.InputCommandPrefix.setPlaceholderText(
            _translate("MainWindow", "Префикс команд"))
        self.MainGroupLabel.setText(_translate("MainWindow", "Основное"))
        self.TextGroupLabel.setText(_translate("MainWindow", "Текст"))
        self.ChannelSpamText.setPlaceholderText(
            _translate("MainWindow", "Текст для спама"))
        self.BanReason.setPlaceholderText(
            _translate("MainWindow", "Причина бана"))
        self.NewServerName.setPlaceholderText(
            _translate("MainWindow", "Новое имя сервера"))
        self.RolesName.setPlaceholderText(_translate("MainWindow",
                                                     "Имя ролей"))
        self.DMSpam.setPlaceholderText(
            _translate("MainWindow", "Текст для спама в ЛС всем участникам"))
        self.MessageOnStart.setPlaceholderText(
            _translate("MainWindow", "Текст при запуске бота"))
        self.EnableMessageOnStart.setToolTip(
            _translate("MainWindow",
                       "Определает, отправлять ли сообщение при вводе !nuke"))
        self.EnableDMSpam.setToolTip(
            _translate(
                "MainWindow",
                "Определает, спамить ли всем участникам в ЛС (ЕСЛИ СЕРВЕР БОЛЬШОЙ НЕ ВКЛЮЧАЙТЕ)"
            ))
        self.EnableCDRoles.setToolTip(
            _translate("MainWindow",
                       "Определяет, требуется ли пересоздавать роли"))
        self.EnableServerRename.setToolTip(
            _translate("MainWindow",
                       "Определяет, требуется ли переименовывать сервер"))
        self.EnableMassban.setToolTip(
            _translate("MainWindow",
                       "Определяет, устраивалить ли массовый бан"))
        self.EnableTotalSpam.setToolTip(
            _translate(
                "MainWindow",
                "Определяет, будет ли спам-бот отправлять сообщения во все существующие/новые каналы"
            ))
        self.OtherGroupLabel.setText(
            _translate("MainWindow", "Другие настройки"))
        self.EnableRandomChannelsType.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Если включено пересоздание каналов!</p><p>Если не включено - создаёт только текстовые каналы</p><p>Если включено - создаёт текстовый или голосовой канал, или категорию</p></body></html>"
            ))
        self.EnableRandomChannelsTypeLabel.setText(
            _translate("MainWindow", "Включить рандомный тип каналов"))
        self.EnableChannelPurge.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Можно использовать для троллинга</p></body></html>"
            ))
        self.ChannelPurgeLabel.setText(
            _translate("MainWindow",
                       "Очистить канал где была отправлена команда"))
        self.EnableEmojiRemover.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>На сервере будут удалены все эмодзи</p></body></html>"
            ))
        self.RemoveEmojisLabel.setText(
            _translate("MainWindow", "Удалить все эмодзи на сервере"))
        self.EnableInvitesRemover.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>На сервере будут удалены все приглашения</p></body></html>"
            ))
        self.RemoveInvitesLabel.setText(
            _translate("MainWindow", "Удалить все приглашения на сервере"))
        self.EnableWebhooksCreator.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>На сервере будет создано ОЧЕНЬ много вебхуков</p></body></html>"
            ))
        self.CreateWebhooksLabel.setText(
            _translate("MainWindow", "Создавать вебхуки"))
        self.EnableWebhooksFlooder.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Спамить вебхуками которые будут созданы</p></body></html>"
            ))
        self.SpamWebhooksLabel.setText(
            _translate("MainWindow", "Спамить вебхуками"))
        self.EnableRemoveServerTemplate.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Удалить ли шаблон сервера?</p></body></html>"
            ))
        self.DeleteTemplateLabel.setText(
            _translate("MainWindow", "Удалить все шаблоны сервера"))
        self.EnableChangeServerIcon.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Сменить иконку сервера?</p></body></html>"
            ))
        self.ChangeIconLabel.setText(
            _translate("MainWindow", "Сменить иконку сервера"))
        self.NewServerIconFileName.setPlaceholderText(
            _translate("MainWindow", "Имя файла новой иконки сервера"))
        self.AutoLeaveGroupLabel.setText(_translate("MainWindow",
                                                    "Авто-выход"))
        self.EnableAutoLeave.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Бот выйдет из сервера через указанное время</p></body></html>"
            ))
        self.EnableAutoLeaveLabel.setText(_translate("MainWindow", "Включить"))
        self.AutoLeave_LeaveAfter.setPlaceholderText(
            _translate("MainWindow", "Активировать через (сек)"))
        self.ExcludesGroupLabel.setText(_translate("MainWindow", "Исключения"))
        self.BanExcludes.setPlaceholderText(
            _translate("MainWindow",
                       "Кого не нужно банить (по одному тегу на строку)"))
        self.SpamWebhooksName.setPlaceholderText(
            _translate("MainWindow",
                       "Имена для спам-вебхуков (по одному имени на строку)"))
        self.CreateConfig.setText(_translate("MainWindow", "СОЗДАТЬ"))
        self.NewChannelsName.setPlaceholderText(
            _translate("MainWindow", "Имя для новых каналов"))
        self.EnableCDChannels.setToolTip(
            _translate(
                "MainWindow",
                "Определает, спамить ли всем участникам в ЛС (ЕСЛИ СЕРВЕР БОЛЬШОЙ НЕ ВКЛЮЧАЙТЕ)"
            ))

        self.CreateConfig.clicked.connect(self.Create)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Create(self):
        # create a dict
        config = {
            # Токен бота
            # str -> TOKEN
            'BOT_TOKEN': 'ТОКЕН БОТА',

            # Префикс для команд бота
            # str
            'BOT_COMMAND_PREFIX': '!',

            # Имя для каналов крашера
            # str
            'CHANNELS_NAME': 'КРАШ СЕРВЕРА',

            # Текст для спама
            # str
            'SPAM_TEXT': '@everyone ВЫПОЛНЯЕТСЯ КРАШ СЕРВЕРА! :clown:',

            # Причина для бана
            # str
            'BAN_REASON': 'Просто так',

            # Новое имя для сервера
            # str
            'RENAME_SERVER_TO': 'СЕРВЕР КРАШНУТ🤡',

            # Новое имя для ролей
            # str
            'ROLES_NAME': 'КРАШ',

            # Спам участникам в ЛС
            # str
            'DM_SPAM': 'ВЫПОЛНЯЕТСЯ КРАШ СЕРВЕРА!',

            # Сообщение при запуске крашера
            # str
            'NUKER_START_MESSAGE': '''@everyone
        Уважаемые участники данного сервера!
        К сожалению, админ или модератор этого сервера оказался 🦣ом, и добавил меня на сервер :clap:
        Краш сервера начнётся через 3 секунды! :clown:''',

            # Отправлять ли стартовое сообщение?
            # bool -> True|False
            'SHOW_START_MESSAGE': False,

            # Автоматически выходить из сервера после указанного времени
            # bool -> True|False
            'AUTO_LEAVE': False,

            # Через сколько автоматически уходить с сервера
            # int -> Seconds
            'AUTO_LEAVE_SEC': 240,
            'NUKER_OPTIONS': {

                # Переименовывать сервер?
                # bool -> True|False
                'RENAME_GUILD': False,

                # Очистить сообщения?
                # bool -> True|False
                'PURGE': False,

                # Спамить участникам в ЛС?
                # Рекомендую оставить False, если на сервере больше 100 участников.
                # bool -> True|False
                'FLOOD_DM': False,

                # Удалить все каналы, и создать новые?
                # bool -> True|False
                'CREATE_CHANNELS': False,

                # False - создаёт только текстовые каналы
                # False - создаёт {текстовый канал|голосовой канал|категорию}
                # bool -> True|False
                'CHANNELS_TYPE_RANDOM': False,

                # Пересоздать ли роли?
                # bool -> True|False
                'CDROLES': False,

                # Банить ли участников?
                # bool -> True|False
                'BAN_MEMBERS': False,

                # Удалять ли эмодзи?
                # bool -> True|False
                'DELETE_EMOJIS': False,

                # Удалять ли приглашения?
                # bool -> True|False
                'DELETE_INVITES': False,

                # Спамить ли на всех каналах?
                # bool -> True|False
                'TOTAL_SPAM': False,

                # Создавать ли много вебхуков?
                # bool -> True|False
                'CREATE_WEBHOOKS': False,

                # Спамить ли вебхуками?
                # bool -> True|False
                'SPAM_WEBHOOKS': False,

                # Удалять ли шаблоны?
                # bool -> True|False
                'DELETE_TEMPLATES': False,

                # Менять ли иконку сервера?
                # bool -> True|False
                'CHANGE_SERVER_ICON': False,

                # Файл с иконкой сервера
                'SERVER_ICON': 'sample.png'
            },

            # Участники, которых не нужно банить.
            # array list[str -> example#0000, ...]
            'BAN_EXCLUDES': [],

            # Имена для вебхуков
            # array list[str, ...]
            'WEBHOOK_NAMES': []
        }

        # setup token
        config['BOT_TOKEN'] = self.TokenInput.text()

        # setup command prefix
        config['COMMAND_PREFIX'] = self.InputCommandPrefix.text()

        # setup spam text
        config['SPAM_TEXT'] = self.ChannelSpamText.text()

        # setup ban reason
        config['BAN_REASON'] = self.BanReason.text()

        # setup server name
        config['RENAME_SERVER_TO'] = self.NewServerName.text()

        # setup roles name
        config['ROLES_NAME'] = self.RolesName.text()

        # setup DM spam
        config['DM_SPAM'] = self.DMSpam.text()

        # setup start message
        config['NUKER_START_MESSAGE'] = self.MessageOnStart.toPlainText()

        # setup webhooks name
        webhooks_names = self.SpamWebhooksName.toPlainText().split('\n')
        config['WEBHOOK_NAMES'] = webhooks_names

        # setup server icon file name
        config['NUKER_OPTIONS'][
            'SERVER_ICON'] = self.NewServerIconFileName.text()

        # setup auto exit time in secs
        try:
            config['AUTO_LEAVE_SEC'] = int(self.AutoLeave_LeaveAfter.text())
        except:
            if self.EnableAutoLeave.isChecked():
                MessageBox(
                    'Ошибка',
                    'Не удалось переобразовать AutoLeave_LeaveAfter в int -> seconds'
                )
                return

        # setup ban excludes
        ban_excludes = self.BanExcludes.toPlainText().split('\n')
        config['BAN_EXCLUDES'] = ban_excludes

        # setup total spam
        config['NUKER_OPTIONS']['TOTAL_SPAM'] = self.EnableTotalSpam.isChecked(
        )

        if self.EnableTotalSpam.isChecked() and self.ChannelSpamText.text(
        ) == '':
            MessageBox(
                'Ошибка',
                'ChannelSpamText не может быть пустым, если EnableTotalSpam включен'
            )
            return

        # setup massban
        config['NUKER_OPTIONS']['BAN_MEMBERS'] = self.EnableMassban.isChecked()

        if self.EnableMassban.isChecked() and self.BanReason.text() == '':
            MessageBox(
                'Ошибка',
                'BanReason не может быть пустым, если EnableMassban включен')
            return

        # setup guild rename
        config['NUKER_OPTIONS'][
            'RENAME_GUILD'] = self.EnableServerRename.isChecked()

        if self.EnableServerRename.isChecked() and self.NewServerName.text(
        ) == '':
            MessageBox(
                'Ошибка',
                'NewServerName не может быть пустым, если EnableServerRename включен'
            )
            return

        # setup role spam
        config['NUKER_OPTIONS']['CDROLES'] = self.EnableCDRoles.isChecked()

        if self.EnableCDRoles.isChecked() and self.RolesName.text() == '':
            MessageBox(
                'Ошибка',
                'RolesName не может быть пустым, если EnableCDRoles включен')
            return

        # setup DM spam
        config['NUKER_OPTIONS']['FLOOD_DM'] = self.EnableDMSpam.isChecked()

        if self.EnableDMSpam.isChecked() and self.DMSpam.text() == '':
            MessageBox(
                'Ошибка',
                'DMSpam не может быть пустым, если EnableDMSpam включен')
            return

        # setup channels name
        config['CHANNELS_NAME'] = self.NewChannelsName.text()

        # setup cd channels
        config['NUKER_OPTIONS'][
            'CREATE_CHANNELS'] = self.EnableCDChannels.isChecked()

        if self.EnableCDChannels.isChecked() and self.NewChannelsName.text(
        ) == '':
            MessageBox(
                'Ошибка',
                'NewChannelsName не может быть пустым, если EnableCDChannels включен'
            )
            return

        # setup start message
        config['SHOW_START_MESSAGE'] = self.EnableMessageOnStart.isChecked()

        if self.EnableMessageOnStart.isChecked(
        ) and self.MessageOnStart.toPlainText() == '':
            MessageBox(
                'Ошибка',
                'MessageOnStart не может быть пустым, если EnableMessageOnStart включен'
            )
            return

        # setup random channels type
        config['NUKER_OPTIONS'][
            'CHANNELS_TYPE_RANDOM'] = self.EnableRandomChannelsType.isChecked(
            )

        # setup purge
        config['NUKER_OPTIONS']['PURGE'] = self.EnableChannelPurge.isChecked()

        # setup emoji remove
        config['NUKER_OPTIONS'][
            'DELETE_EMOJIS'] = self.EnableEmojiRemover.isChecked()

        # setup delete invites
        config['NUKER_OPTIONS'][
            'DELETE_INVITES'] = self.EnableInvitesRemover.isChecked()

        # setup create webhooks
        config['NUKER_OPTIONS'][
            'CREATE_WEBHOOKS'] = self.EnableWebhooksCreator.isChecked()

        # setup webhooms flood
        config['NUKER_OPTIONS'][
            'SPAM_WEBHOOKS'] = self.EnableWebhooksFlooder.isChecked()

        # setup delete templates
        config['NUKER_OPTIONS'][
            'DELETE_TEMPLATES'] = self.EnableRemoveServerTemplate.isChecked()

        # setup change server icon
        config['NUKER_OPTIONS'][
            'CHANGE_SERVER_ICON'] = self.EnableChangeServerIcon.isChecked()

        if self.EnableChangeServerIcon.isChecked(
        ) and self.NewServerIconFileName.text() == '':
            MessageBox(
                'Ошибка',
                'NewServerIconFileName не может быть пустым, если ChangeServerIcon включен'
            )
            return

        # setup auto leave
        config['NUKER_OPTIONS']['AUTO_LEAVE'] = self.EnableAutoLeave.isChecked(
        )

        file = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить конфиг',
                                                     'nuker.py')[0]

        if file == '':
            return

        file = open(file, 'w', encoding='utf-8')
        file.write(str(config))
        file.close()


class ApplicationWindow(ApplicationMainWindow):

    def __init__(self):
        super().__init__()
        self.WindowInit(self)

    def closeEvent(self, *args):
        exit(0)


from sys import argv

if __name__ == "__main__":
    Application = QtWidgets.QApplication(argv)
    Window = ApplicationWindow()
    Window.show()
    exit(Application.exec_())