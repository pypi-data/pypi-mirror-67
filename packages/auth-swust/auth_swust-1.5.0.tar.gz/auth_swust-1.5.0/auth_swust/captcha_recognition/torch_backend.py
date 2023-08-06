import string
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F


class LeNet5(nn.Module):
    def __init__(self):
        super(LeNet5, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 3)
        self.conv2 = nn.Conv2d(6, 16, 3)

        self.fc1 = nn.Linear(576, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 36)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))
        x = x.view(-1, self.num_flat_features(x))

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
        # return F.log_softmax(x, dim=1)

    def num_flat_features(self, x):
        # 相当于flatten
        size = x.size()[1:]  # 除去批处理维度的其他所有维度
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


# 使用绝对路径 设置model的位置
model_path = str(Path(__file__).parent.joinpath("model", "captcha_cnn.pth"))

state_dict = torch.load(model_path)
net = LeNet5()
net.eval()
net.load_state_dict(state_dict)

label_list = string.digits + string.ascii_uppercase


def decode(index):
    return label_list[index]


def _predict(subimages):
    t = []
    all = None
    s = ""
    for i, x in enumerate(subimages, 0):
        t.append(torch.from_numpy(subimages[i]).view(-1, 1, 32, 32).to(torch.float32))
        if i == 3:
            all = torch.cat(t)
    for x in range(4):
        s += decode(net(all)[x].argmax())
    return s
