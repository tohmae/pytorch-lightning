# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pytorch_lightning.plugins.strategy.ipu import IPUPlugin
from pytorch_lightning.utilities import rank_zero_deprecation


class IPUPlugin(IPUPlugin):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        rank_zero_deprecation(
            "`pytorch_lightning.plugins.training_type.ipu.IPUPlugin` has been deprecated in v1.6"
            " and will be removed in v1.8. Use `pytorch_lightning.plugins.strategy.ipu.IPUPlugin`"
            " instead."
        )
