# -*- coding: utf-8 -*-
#
# This file is a part of Typhoon HIL API library.
#
# Typhoon HIL API is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from typhoon.api.configuration_manager.base import ConfigurationManagerAPIBase
from typhoon.api.configuration_manager.stub import clstub
from typhoon.api.utils import determine_path


# noinspection PyMethodMayBeStatic
class ConfigurationManagerAPI(ConfigurationManagerAPIBase):

    def save_config(self, config_handle, save_path):
        """
        Saves an existing configuration to a file.

        Args:
            config_handle(ItemHandle): Handle to the configuration to save.
            save_path(str): Path to directory/file where to save the
              configuration.

        Returns:
            None
                """
        return clstub().save_config(config_handle=config_handle,
                                    save_path=determine_path(save_path))

    def create_config(self, config_name):
        """
        Creates a new configuration.

        Args:
            config_name(str): Configuration name.

        Returns:
            Handle to configuration object.
        """
        return clstub().create_config(config_name=config_name)

    def generate(self, project_handle, config_handle, out_dir="",
                 file_name="", standalone_model=True):
        """
        Generates the specified project using the specified configuration.

        Args:
            project_handle: Project to generate.
            config_handle: The configuration handle which is to be generated.
            out_dir: Directory (absolute or relative) where to save the
                resulting .tse file
            file_name: Name of the file where to save the resulting .tse file.
                Should only be the name of the file, and not contain any
                directory parts.
            standalone_model(bool): Specify should generated model be
                self-contained (independent from any user/custom libraries)

        Returns:
            GenerateResult object (which contains path to generated model).
                """
        # -- Only the output directory needs to be determined
        # -- The file name should only be a file name, and not contain any
        # folder parts
        out_dir_intermediate = determine_path(out_dir)
        return clstub().generate(project_handle=project_handle,
                                 config_handle=config_handle,
                                 out_dir=out_dir_intermediate,
                                 file_name=file_name,
                                 standalone_model=standalone_model)

    def load_config(self, config_path):
        """
        Loads an existing configuration from the specified configuration file.

        Args:
            config_path(str): Path to existing configuration file (.tcfg)

        Returns:
            Handle to the loaded configuration.
        """
        return clstub().load_config(config_path=determine_path(config_path))

    def load_project(self, project_path):
        """
        Loads a project from the specified project file.

        Args:
            project_path(str): Path to an existing project file (.tcp)

        Returns:
            Handle to the loaded project.
        """
        return clstub().load_project(project_path=determine_path(project_path))

    def make_pick(self, variant_name, option_name,
                  option_configuration=None):
        """
        Creates a pick object that can be used in conjunction with
        the picks method.

        Args:
            variant_name(str): Name of the configuration variant
              (component placeholder) to be picked.
            option_name(str): Name of an existing option from the
              selected variant.
            option_configuration(dict): Dictionary of property names and
                values, which will be used to override option component
                property values.

        Returns:
            Handle to a pick object.
        """
        return clstub().make_pick(variant_name=variant_name,
                                  option_name=option_name,
                                  option_configuration=option_configuration)

    def picks(self, config_handle, pick_handles):
        """
        Insert provided picks into a configuration specified by
        ``config_handle.``

        Args:
            config_handle(ItemHandle): Handle to configuration object
            pick_handles(list): List of pick handles for substitution.

        Returns:
            None
        """
        if not (isinstance(pick_handles, (list, tuple)) and \
                all(isinstance(i, dict) for i in pick_handles)):
            raise TypeError(
                "Function picks() expects ``pick_handles`` argument"
                " to be a list (or tuple) of Pick objects."
            )
        clstub().picks(config_handle=config_handle, pick_handles=pick_handles)

    def get_name(self, item_handle):
        """
        Returns name for item specified by ``item_handle``.
        Item should have name.

        Args:
            item_handle(ItemHandle): ItemHandle object.

        Returns:
            Name as str.

        Raises:
            ConfigurationManagerAPIException if ``item_handle`` is invalid (
            wrong type or doesn't have name)
        """
        return clstub().get_name(item_handle=item_handle)
